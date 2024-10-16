import cx_Oracle
from db_config import DB_CONFIG
import traceback

def create_table():
    connection = None
    try:
        connection = cx_Oracle.connect(**DB_CONFIG)
        cursor = connection.cursor()
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
            connection.close()

def insert_data(location, date_time, temperature, precipitation):
    connection = None
    try:
        connection = cx_Oracle.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO climate_data (location, date_time, temperature, precipitation)
            VALUES (:1, :2, :3, :4)
        """, (location, date_time, temperature, precipitation))
        connection.commit()
        print("Data inserted successfully")
    except cx_Oracle.Error as error:
        print(f"Error inserting data: {error}")
    finally:
        if connection:
            connection.close()

def get_unique_locations():
    connection = None
    try:
        print("Conectando ao banco de dados para obter localizações únicas")
        connection = cx_Oracle.connect(**DB_CONFIG)
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
            connection.close()
            print("Conexão fechada após obter localizações únicas")

def fetch_data(location):
    connection = None
    try:
        print(f"Conectando ao banco de dados para buscar dados de {location}")
        connection = cx_Oracle.connect(**DB_CONFIG)
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
            connection.close()
            print(f"Conexão fechada após buscar dados para {location}")

def delete_all_data():
    connection = None
    try:
        connection = cx_Oracle.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM climate_data")
        connection.commit()
        print("All data deleted successfully")
    except cx_Oracle.Error as error:
        print(f"Error deleting all data: {error}")
    finally:
        if connection:
            connection.close()

def update_data(location, date_time, temperature, precipitation):
    connection = None
    try:
        connection = cx_Oracle.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE climate_data
            SET temperature = :1, precipitation = :2
            WHERE location = :3 AND date_time = :4
        """, (temperature, precipitation, location, date_time))
        connection.commit()
        print("Data updated successfully")
    except cx_Oracle.Error as error:
        print(f"Error updating data: {error}")
    finally:
        if connection:
            connection.close()

def delete_data(location, date_time):
    connection = None
    try:
        connection = cx_Oracle.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM climate_data
            WHERE location = :1 AND date_time = :2
        """, (location, date_time))
        connection.commit()
        print("Data deleted successfully")
    except cx_Oracle.Error as error:
        print(f"Error deleting data: {error}")
    finally:
        if connection:
            connection.close()

# Initialize the database
create_table()
