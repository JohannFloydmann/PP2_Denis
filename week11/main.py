import DB as db
import funcs as f


if __name__ == '__main__':
    
    db.create_table()
    
    db.get_all_users()
    f.get_users_paginated(1, 5)
    f.get_users_paginated(2, 5)

    db.close_connection()