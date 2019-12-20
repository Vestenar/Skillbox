from brute import start_bruteforce
"""
Предполагается, что пароль пользователя начинается состоит из имени пользователя, которое
совпадает с логином почтовой системы, и дополняется случайной цифро-буквенной комбинацией 
"""

login = 'skillbox@mail.ru'
pass_pattern = login.split('@')[0]

if __name__ == '__main__':
    start_bruteforce(login, pass_pattern)