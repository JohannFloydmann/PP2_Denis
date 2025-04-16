import psycopg2
import json
from DB.config import load_config

# connect to db
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

config = load_config()
conn = connect(config) # create connection varibale
 
def create_table():
    # create table    
    command = """
        CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            save JSONB
        )
        """
    try:
        with conn.cursor() as cur:
            # execute the commands
            cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
        
def get_all_users():
    # Retrieve data from the Users table
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Users")
            rows = cur.fetchall()
            print("The number of users: ", cur.rowcount)
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def check_if_user_exists(name):
    command = "SELECT user_name FROM Users WHERE user_name = %s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            result = cur.fetchall()
            return bool(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def login(user_name):
    if check_if_user_exists(user_name):
        print(f"User {user_name} exists.")
        command = """SELECT save FROM Users WHERE user_name = %s"""
        try:
            with conn.cursor() as cur:
                cur.execute(command, (user_name,))
                row = cur.fetchone()
                return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    else:
        create_user(user_name)


def get_user_by_name(name):
    # get user by name
    command = """SELECT user_name FROM Users WHERE user_name = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            rows = cur.fetchall()
            print("The number of users: ", cur.rowcount)
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_user(name):
    # insert user
    command = """INSERT INTO Users(user_name) VALUES(%s)"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
            print(f"Inserted {cur.rowcount} row(s)")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def load_save(name, save):
    # insert user
    command = """UPDATE Users SET save = %s WHERE user_name = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (json.dumps(save), name))
            conn.commit()
            print(f"Inserted {cur.rowcount} row(s)")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_save(name):
    # get user save
    command = """SELECT save FROM Users WHERE user_name = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            row = cur.fetchone()
            print(row)
            return row[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_by_name(name, telephone):
    # update user by name
    command = """UPDATE Users SET user_phone = %s WHERE user_name = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (telephone, name))
            conn.commit()
            print(f"Updated {cur.rowcount} row(s)")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_by_name(name):
    # delete user by name
    command = """DELETE FROM Users WHERE user_name = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
            print(f"Deleted {cur.rowcount} row(s)")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_all_users():
    # delete all users
    command = """DELETE FROM Users"""
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
            print(f"Deleted {cur.rowcount} row(s)")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def drop_table():
    # drop table
    command = """DROP TABLE IF EXISTS Users"""
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
            print("Table dropped.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def close_connection():
    # close connection
    conn.close()
    print('Connection closed.')

if __name__ == '__main__':
    
    create_table()
    d = {'level': 1, 'score': 100}
    load_save('test_user', d)

    get_all_users()
    close_connection()