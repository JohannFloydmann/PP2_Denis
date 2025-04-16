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

def csv_to_table(filename):
    # csv file to db insert   
    command = f"""INSERT INTO Users(user_name, user_phone) VALUES(%s, %s)"""
    try:
        with conn.cursor() as cur:
            # execute the command
            with open(filename, "r") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                for row in csvreader:
                    # print(row)
                    name, telephone = row
                    # print(id, name, telephone)
                    cur.execute(command, (name, telephone))
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


if __name__ == '__main__':
    
    create_table()
    csv_to_table("users.csv")
    get_all_users()