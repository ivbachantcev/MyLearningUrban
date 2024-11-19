class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
    

class User:
    '''
    Класс пользователя, содержащий атрибуты: логин, пароль
    '''
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.passsword = password



if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Hi. Выберите действие: \n1-логин\n2-регистрация\n'))
        if choice == 1:
            login = input('Login:')
            password = input('Password:')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполен, {login}.')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('User not found')
        if choice == 2:
            user = User(input('Login:'), password := input('Password:'), password2 := input('Confirm password: '))
            if password != password2:
                print('Пароли не совпадают, попробуйте ещё раз')
                continue
            database.add_user(user.username, user.passsword)
        print(database.data)