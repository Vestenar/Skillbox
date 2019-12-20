from brute import start_bruteforce
"""
Предполагается, что логин пользователя в почтовой системе включает в себя дату рождения пользователя, 
а пароль состоит из даты рождения пользователя (без разделителей) и дополняется случайной цифро-буквенной комбинацией 
"""

login = 'nikita01_02_1985@skillbox.com'
state = 0
pass_pattern = ''.join([i for i in login if i.isdigit()])


if __name__ == '__main__':
    start_bruteforce(login, pass_pattern)