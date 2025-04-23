import DB as db
import psycopg2

# creatre functions
def create_search_users_function():
    #  Create a PostgreSQL function to search Users by pattern in user_name or user_phone.
    command = """
    CREATE OR REPLACE FUNCTION search_users_by_pattern(p_pattern VARCHAR)
    RETURNS TABLE (
        id INTEGER,
        user_name VARCHAR,
        user_phone VARCHAR
    ) AS $$
    BEGIN
        RETURN QUERY
        SELECT u.id, u.user_name, u.user_phone
        FROM Users u
        WHERE u.user_name ILIKE '%' || p_pattern || '%'
           OR u.user_phone ILIKE '%' || p_pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("PostgreSQL function 'search_users_by_pattern' created or replaced.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# create procedures
def create_upsert_user_procedure():

    # Create a PostgreSQL procedure to insert a new user or update phone if user exists.

    command = """
    CREATE OR REPLACE PROCEDURE upsert_user(
        p_user_name VARCHAR,
        p_user_phone VARCHAR
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        -- Check if user_name exists, and if so, update the phone
        IF EXISTS (SELECT 1 FROM Users WHERE user_name = p_user_name) THEN
            UPDATE Users
            SET user_phone = p_user_phone
            WHERE user_name = p_user_name;
            
        -- Check if user_phone exists, and if so, update the name
        ELSIF EXISTS (SELECT 1 FROM Users WHERE user_phone = p_user_phone) THEN
            UPDATE Users
            SET user_name = p_user_name
            WHERE user_phone = p_user_phone;
            
        -- If neither exists, insert a new user
        ELSE
            INSERT INTO Users (user_name, user_phone)
            VALUES (p_user_name, p_user_phone);
        END IF;
    END;
    $$;
    """
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("PostgreSQL procedure 'upsert_user' created or replaced.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_insert_many_users_function():
    """
    Create a PostgreSQL function to insert multiple users, validate phones,
    and return invalid entries.
    """
    command = """
    CREATE OR REPLACE FUNCTION insert_many_users(
        p_names VARCHAR[],
        p_phones VARCHAR[]
    )
    RETURNS JSONB
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INTEGER;
        total_length INTEGER;
        invalid_data JSONB := '[]'::JSONB;
        current_name VARCHAR;
        current_phone VARCHAR;
        is_valid_phone BOOLEAN;
    BEGIN
        -- Check if arrays have the same length
        total_length := array_length(p_names, 1);
        IF total_length IS NULL OR total_length != array_length(p_phones, 1) THEN
            RAISE EXCEPTION 'Input arrays must have the same length';
        END IF;

        -- Loop through the arrays
        FOR i IN 1..total_length LOOP
            current_name := p_names[i];
            current_phone := p_phones[i];

            -- Validate phone number (e.g., XXX-XXX-XXXX or 10 digits)
            is_valid_phone := current_phone ~ '^[0-9]{3}-[0-9]{3}-[0-9]{4}$' OR current_phone ~ '^[0-9]{10}$';

            IF is_valid_phone THEN
                -- Insert valid user
                BEGIN
                    INSERT INTO Users (user_name, user_phone)
                    VALUES (current_name, current_phone);
                EXCEPTION WHEN unique_violation THEN
                    -- Skip if phone already exists (due to UNIQUE constraint)
                    invalid_data := invalid_data || jsonb_build_object(
                        'name', current_name,
                        'phone', current_phone,
                        'error', 'Phone number already exists'
                    );
                END;
            ELSE
                -- Add to invalid entries if phone is invalid
                invalid_data := invalid_data || jsonb_build_object(
                    'name', current_name,
                    'phone', current_phone,
                    'error', 'Invalid phone format (expected XXX-XXX-XXXX or 10 digits)'
                );
            END IF;
        END LOOP;

        -- Return the invalid entries
        RETURN invalid_data;
    END;
    $$;
    """
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("PostgreSQL function 'insert_many_users' created or replaced.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_get_users_paginated_function():

    # Create a PostgreSQL function to query Users with pagination.

    command = """
    CREATE OR REPLACE FUNCTION get_users_paginated(
        p_limit INTEGER,
        p_offset INTEGER
    )
    RETURNS TABLE (
        id INTEGER,
        user_name VARCHAR,
        user_phone VARCHAR
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT u.id, u.user_name, u.user_phone
        FROM Users u
        ORDER BY u.id
        LIMIT p_limit
        OFFSET p_offset;
    END;
    $$;
    """
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("PostgreSQL function 'get_users_paginated' created or replaced.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def create_delete_user_function():
    """
    Create a PostgreSQL function to delete a user by user_name or user_phone.
    """
    command = """
    CREATE OR REPLACE FUNCTION delete_user(
        p_user_name VARCHAR,
        p_user_phone VARCHAR
    )
    RETURNS INTEGER
    LANGUAGE plpgsql
    AS $$
    DECLARE
        deleted_rows INTEGER := 0;
    BEGIN
        -- Delete by user_name if provided
        IF p_user_name IS NOT NULL THEN
            DELETE FROM Users
            WHERE user_name = p_user_name;
            GET DIAGNOSTICS deleted_rows = ROW_COUNT;
        
        -- Otherwise, delete by user_phone if provided
        ELSIF p_user_phone IS NOT NULL THEN
            DELETE FROM Users
            WHERE user_phone = p_user_phone;
            GET DIAGNOSTICS deleted_rows = ROW_COUNT;
        END IF;

        RETURN deleted_rows;
    END;
    $$;
    """
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("PostgreSQL function 'delete_user' created or replaced.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_drop_all_functions_procedures_function():
    """
    Create a PostgreSQL function to drop all user-defined functions and procedures.
    """
    command = """
    CREATE OR REPLACE FUNCTION drop_all_functions_procedures()
    RETURNS VOID
    LANGUAGE plpgsql
    AS $$
    DECLARE
        rec RECORD;
        drop_stmt TEXT;
    BEGIN
        -- Loop through all user-defined functions and procedures in the public schema
        FOR rec IN (
            SELECT 
                n.nspname AS schema_name,
                p.proname AS function_name,
                pg_get_function_arguments(p.oid) AS args,
                CASE 
                    WHEN p.prokind = 'p' THEN 'PROCEDURE'
                    ELSE 'FUNCTION'
                END AS routine_type
            FROM pg_proc p
            JOIN pg_namespace n ON p.pronamespace = n.oid
            WHERE n.nspname NOT IN ('pg_catalog', 'information_schema')
        ) LOOP
            -- Construct the DROP statement
            drop_stmt := 'DROP ' || rec.routine_type || ' IF EXISTS ' || 
                         quote_ident(rec.schema_name) || '.' || quote_ident(rec.function_name) || 
                         '(' || rec.args || ') CASCADE';
            
            -- Execute the DROP statement
            EXECUTE drop_stmt;
        END LOOP;
    END;
    $$;
    """
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("PostgreSQL function 'drop_all_functions_procedures' created or replaced.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# functions to call postgreSQL functions
def search_users_by_pattern(pattern):
    # Call the PostgreSQL function to search for users by pattern in user_name or user_phone.

    command = """SELECT * FROM search_users_by_pattern(%s)"""
    try:
        with db.conn.cursor() as cur:
            cur.execute(command, (pattern,))
            rows = cur.fetchall()
            print("The number of users: ", cur.rowcount)
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def upsert_user(name, phone):

    #  Call the PostgreSQL procedure to insert a new user or update phone if user exists.

    command = "CALL upsert_user(%s, %s)"
    try:
        with db.conn.cursor() as cur:
            cur.execute(command, (name, phone))
            db.conn.commit()
            print(f"Upserted user: {name}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_many_users(names, phones):

    # Call the PostgreSQL function to insert multiple users and return invalid entries.

    command = "SELECT insert_many_users(%s, %s)"
    try:
        with db.conn.cursor() as cur:
            # Execute the function and fetch the invalid entries
            cur.execute(command, (names, phones))
            invalid_entries = cur.fetchone()[0]  # Fetch the returned JSONB

            # Count successfully inserted users by checking the table
            cur.execute("SELECT COUNT(*) FROM Users WHERE user_phone = ANY(%s)", (phones,))
            inserted_count = cur.fetchone()[0]

            # Print results
            print(f"Inserted {inserted_count} user(s) successfully.")
            if invalid_entries != '[]':
                print("Invalid entries:", invalid_entries)
            else:
                print("No invalid entries.")

            db.conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        db.conn.rollback()

def get_users_paginated(limit, offset):

    # Call the PostgreSQL function to query users with pagination.one: Prints the retrieved records and the count of users returned.

    command = "SELECT * FROM get_users_paginated(%s, %s)"
    try:
        with db.conn.cursor() as cur:
            cur.execute(command, (limit, offset))
            rows = cur.fetchall()
            print("The number of users: ", cur.rowcount)
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_user(user_name=None, user_phone=None):
    """
    Call the PostgreSQL function to delete a user by user_name or user_phone.
    
    Args:
        user_name (str, optional): The user's name to delete by.
        user_phone (str, optional): The user's phone number to delete by.
    
    Returns:
        None: Prints the number of deleted rows.
    """
    command = "SELECT delete_user(%s, %s)"
    try:
        with db.conn.cursor() as cur:
            cur.execute(command, (user_name, user_phone))
            deleted_count = cur.fetchone()[0]  # Fetch the returned INTEGER
            print(f"Deleted {deleted_count} row(s)")
            db.conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        db.conn.rollback()

def drop_all_functions_procedures():
    """
    Call the PostgreSQL function to drop all user-defined functions and procedures.
    
    Returns:
        None: Prints a confirmation message.
    """
    command = "SELECT drop_all_functions_procedures()"
    try:
        with db.conn.cursor() as cur:
            cur.execute(command)
            db.conn.commit()
            print("All user-defined functions and procedures have been dropped.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        db.conn.rollback()


create_drop_all_functions_procedures_function()
drop_all_functions_procedures()

# Call the functions to create PostgreSQL functions and procedures
create_search_users_function()
create_upsert_user_procedure()
create_insert_many_users_function()
create_get_users_paginated_function()
create_delete_user_function()


if __name__ == '__main__':
    db.create_table()

    db.get_all_users()
    delete_user(user_name='John Doe')
    
    db.close_connection()