import psycopg2
import csv
from config import load_config

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
    command = """CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_phone VARCHAR(20) NOT NULL UNIQUE
        )"""
    try:
        with conn.cursor() as cur:
            # execute the command
            cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def read_csv(filename):
    # csv file to db insert   
    command = f"""INSERT INTO Users(user_name, user_phone) VALUES(%s, %s)"""
    try:
        with conn.cursor() as cur:
            # execute the command
            with open(filename, "r") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                rows = 0
                for row in csvreader:
                    # print(row)
                    name, telephone = row
                    # print(id, name, telephone)
                    cur.execute(command, (name, telephone))
                    conn.commit()
                    rows+=1
                print(f"Added rows: {rows}")
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

def get_by_name(name):
    # get user by name
    command = """SELECT * FROM Users WHERE user_name = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            rows = cur.fetchall()
            print("The number of users: ", cur.rowcount)
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_by_phone(phone):
    # get user by phone
    command = """SELECT * FROM Users WHERE user_phone = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (phone,))
            rows = cur.fetchall()
            print("The number of users: ", cur.rowcount)
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_user(name, telephone):
    # insert user
    command = """INSERT INTO Users(user_name, user_phone) VALUES(%s, %s)"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, telephone))
            conn.commit()
            print(f"Inserted {cur.rowcount} row(s)")
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

def update_by_phone(phone, name):
    # update user by phone
    command = """UPDATE Users SET user_name = %s WHERE user_phone = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, phone))
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

def delete_by_phone(phone):
    # delete user by phone
    command = """DELETE FROM Users WHERE user_phone = %s"""
    try:
        with conn.cursor() as cur:
            cur.execute(command, (phone,))
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
    close_connection()