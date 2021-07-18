import sqlite3

class Model(object):
    
    def __init__(self, db_name):
        self.db = sqlite3.connect(f'{db_name}')
        self.sql = self.db.cursor()

        self.sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
            password TEXT,
            cash BIGINT
            )""")

        self.db.commit()

    def register_new_user(self, user_login, user_password):
        '''
        register a new user in database
        '''
        self.sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

        if self.sql.fetchone() is None:
            self.sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
            self.db.commit()

            print('Data has been writing successgully')
        else:
            print('User has already existed!')

    def is_user_exists(self, user_login):
        '''
        check user exists
        return login if user exists
        return None if user doesn't exists
        '''
        self.sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        return self.sql.fetchone()

    def delete_user(self, user_login):
        '''
        delete user from database
        '''
        self.sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
        self.db.commit()

    def get_all_users(self):
        '''
        get tuple of users
        '''
        self.sql.execute("SELECT login, cash FROM users")
        return self.sql.fetchall()

    def get_cash_user(self, user_login):
        '''
        return user's cash value 
        '''
        self.sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'")
        return self.sql.fetchone()[0]

    def update_cash_user(self, user_login, value):
        '''
        Update balance one user
        '''
        balance = self.get_cash_user(user_login)
        
        self.sql.execute(f"UPDATE users SET cash = '{balance + value}' WHERE login = '{user_login}'")
        self.db.commit()

    def __del__(self):
        self.db.close()

