from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver
import time

"""
подключение к серверу: telnet 127.0.0.1 1234
авторизация: login:username
"""


class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    login: str = None

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)
        self.factory.logins.remove(self.login)
        for user in self.factory.clients:
            user.sendLine(f'{self.login} left channel'.encode())

    def lineReceived(self, line: bytes):
        content = line.decode()

        if self.login is not None:
            content = f'Message from {self.login}: {content}'
            self.factory.messages.append([time.asctime().split()[3], content])
            print(self.factory.messages)

            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(content.encode())
        else:
            # login:admin -> admin
            if content.startswith('login:'):
                login = content.replace('login:', '')
                if login not in self.factory.logins:
                    self.login = login
                    for user in self.factory.clients - {self,}:
                        user.sendLine(f'{self.login} joined channel'.encode())
                    self.factory.logins.add(self.login)
                    self.sendLine(f'Welcome, {self.login}'.encode())
                    self.send_history()

                else:
                    self.sendLine('Login busy'.encode())

            else:
                self.sendLine('Invalid login'.encode())

    def send_history(self):
        if self.factory.messages:
            for message in self.factory.messages[-10:]:
                self.sendLine(' -> '.join(message).encode())

class Server(ServerFactory):
    protocol = ServerProtocol
    clients: set
    logins: set
    messages: list

    def startFactory(self):
        self.clients = set()
        self.logins = set()
        self.messages = []
        print('Server Started')

    def stopFactory(self):
        print('Server Stopped')


reactor.listenTCP(1234, Server())
reactor.run()
