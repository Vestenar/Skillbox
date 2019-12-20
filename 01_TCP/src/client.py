from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class ConnectorProtocol(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.sendLine('login:admin'.encode())

    def lineReceived(self, line):
        print(line)


class Connector(ClientFactory):
    protocol = ConnectorProtocol


reactor.connectTCP('localhost', 1234, Connector())
reactor.run()
"""
pyuic5 design.ui -o design.py - конверсия
"""