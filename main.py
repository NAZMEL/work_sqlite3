import sqlite3
from random import randint


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

        print('Data has been writing wuccessfully!')
    else:
        print('User has already existed!')