import sqlite3
from random import randint

global db
global sql

# initializating nonexist database
db = sqlite3.connect('server.db')

# create cursor in the database
sql = db.cursor()


# create table into the database
def create_table():
    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        login TEXT, 
        password TEXT,
        cash BIGINT
    ) """)
    db.commit()


# register a new user
def register_user():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()

        print('Data has been writing successfully!')
    else:
        print('User has already existed!')


def delete_db(user_login):
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()
    
    print('The user was deleted succesfully!')

def casino():
    user_login = input("Log in: ")
    number = randint(1, 2)

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    
    if sql.fetchone() is None:
        print("The user isn't exist. Register now!")
        register_user()
    else:
        sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'")
        balance = sql.fetchone()[0]   # get first value

        if number == 1:
            sql.execute(f"UPDATE users SET cash = {balance + 100} WHERE login = '{user_login}'")
            db.commit()
            print('You are winner!')

        else:
            print('You\'ve lose!')
            delete_db(user_login)


def output():
    sql.execute("SELECT login, cash FROM users")
    [print(row) for row in sql.fetchall()]
    


def main():
    casino()
    output()

if __name__ == '__main__':
    main()