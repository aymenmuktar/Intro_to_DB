import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server (default user and password can be updated)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )
        cursor = conn.cursor()

        # Attempt to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL Server: {err}")
    finally:
        # Cleanup
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()

