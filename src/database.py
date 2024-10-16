import cx_Oracle
from db_config import DB_CONFIG
import traceback
from datetime import datetime

# Create a connection pool
pool = cx_Oracle.SessionPool(
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    dsn=DB_CONFIG['dsn'],
    min=2,
    max=5,
    increment=1,
    threaded=True
)

def create_table():
    connection = None
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        
        # Check if the table already exists
        cursor.execute("""
            SELECT table_name 
            FROM user_tables 
            WHERE table_name = 'CLIMATE_DATA'
        """)
        if cursor.fetchone():
            print("Table 'CLIMATE_DATA' already exists")
            return

        cursor.execute("""
            CREATE TABLE climate_data (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                location VARCHAR2(100),
                date_time TIMESTAMP,
                temperature NUMBER(5,2),
                precipitation NUMBER(5,2)
            )
        """)
        connection.commit()
        print("Table created successfully")
    except cx_Oracle.Error as error:
        print(f"Error creating table: {error}")
    finally:
        if connection:
            pool.release(connection)

def insert_data(location, date_time, temperature, precipitation):
    connection = None
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        # Convert date_time to datetime object if it's a string
        if isinstance(date_time, str):
            try:
                date_obj = datetime.strptime(date_time, "%Y-%m-%d")
            except ValueError:
                date_obj = datetime.strptime(date_time, "%d-%b-%Y %I:%M:%S %p")
        else:
            date_obj = date_time
        cursor.execute("""
            INSERT INTO climate_data (location, date_time, temperature, precipitation)
            VALUES (:1, :2, :3, :4)
        """, (location, date_obj, temperature, precipitation))
        connection.commit()
        print("Data inserted successfully")
    except cx_Oracle.Error as error:
        print(f"Error inserting data: {error}")
    finally:
        if connection:
            pool.release(connection)

def insert_data_batch(data_list):
    connection = None
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.executemany("""
            INSERT INTO climate_data (location, date_time, temperature, precipitation)
            VALUES (:1, :2, :3, :4)
        """, data_list)
        connection.commit()
        print(f"{len(data_list)} records inserted successfully")
    except cx_Oracle.Error as error:
        print(f"Error inserting batch data: {error}")
    finally:
        if connection:
            pool.release(connection)

def get_unique_locations():
    connection = None
    try:
        print("Conectando ao banco de dados para obter localizações únicas")
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT location FROM climate_data")
        locations = [row[0] for row in cursor.fetchall()]
        print(f"Localizações únicas obtidas: {locations}")
        return locations
    except cx_Oracle.Error as error:
        print(f"Erro ao obter localizações únicas: {error}")
        print(traceback.format_exc())
        return []
    finally:
        if connection:
            pool.release(connection)
            print("Conexão fechada após obter localizações únicas")

def fetch_data(location):
    connection = None
    try:
        print(f"Conectando ao banco de dados para buscar dados de {location}")
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT date_time, temperature, precipitation
            FROM climate_data
            WHERE location = :1
            ORDER BY date_time
        """, (location,))
        data = cursor.fetchall()
        print(f"Dados obtidos para {location}: {len(data)} registros")
        return data
    except cx_Oracle.Error as error:
        print(f"Erro ao buscar dados para {location}: {error}")
        print(traceback.format_exc())
        return []
    finally:
        if connection:
            pool.release(connection)
            print(f"Conexão fechada após buscar dados para {location}")

def delete_all_data():
    connection = None
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM climate_data")
        connection.commit()
        print("All data deleted successfully")
    except cx_Oracle.Error as error:
        print(f"Error deleting all data: {error}")
    finally:
        if connection:
            pool.release(connection)

def update_data(location, date_time, temperature, precipitation):
    connection = None
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        # Convert date_time to datetime object if it's a string
        if isinstance(date_time, str):
            try:
                date_obj = datetime.strptime(date_time, "%Y-%m-%d")
            except ValueError:
                date_obj = datetime.strptime(date_time, "%d-%b-%Y %I:%M:%S %p")
        else:
            date_obj = date_time
        cursor.execute("""
            UPDATE climate_data
            SET temperature = :1, precipitation = :2
            WHERE location = :3 AND date_time = :4
        """, (temperature, precipitation, location, date_obj))
        connection.commit()
        print("Data updated successfully")
    except cx_Oracle.Error as error:
        print(f"Error updating data: {error}")
    finally:
        if connection:
            pool.release(connection)

def delete_data(location, date_time):
    connection = None
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        # Convert date_time to datetime object if it's a string
        if isinstance(date_time, str):
            try:
                date_obj = datetime.strptime(date_time, "%Y-%m-%d")
            except ValueError:
                date_obj = datetime.strptime(date_time, "%d-%b-%Y %I:%M:%S %p")
        else:
            date_obj = date_time
        cursor.execute("""
            DELETE FROM climate_data
            WHERE location = :1 AND date_time = :2
        """, (location, date_obj))
        connection.commit()
        print("Data deleted successfully")
    except cx_Oracle.Error as error:
        print(f"Error deleting data: {error}")
    finally:
        if connection:
            pool.release(connection)

# Initialize the database
create_table()
