from model import Model
from random import randint

def main():
    user_login = input("Sign in: ")
    number = randint(1, 100)
    users = Model('server.db')

    if users.is_user_exists(user_login) is None:
        print("The user isn't exist. Register now!")
        user_login = input("Input login: ")
        user_password = input("Input password: ")
        users.register_new_user(user_login, user_password)
    else:
        if number < 50:
            users.update_cash_user(user_login, 100)
            print('You are winner!')
        else:
            print('You lose')
            users.delete_user(user_login)
    
    [print(user) for user in users.get_all_users()]


if __name__ == '__main__':
    main()


