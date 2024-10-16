import cx_Oracle
from db_config import DB_CONFIG

def test_connection():
    try:
        connection = cx_Oracle.connect(**DB_CONFIG)
        print("Successfully connected to Oracle Database")
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM DUAL")
        result = cursor.fetchone()
        print(f"Test query result: {result}")
    except cx_Oracle.Error as error:
        print(f"Error connecting to Oracle Database: {error}")
    finally:
        if 'connection' in locals():
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    test_connection()
