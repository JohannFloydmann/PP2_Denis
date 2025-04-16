import DB as db
if __name__ == '__main__':
    
    db.create_table()
    
    db.delete_all_users()
    db.read_csv('users.csv')
    db.get_all_users()

    db.close_connection()