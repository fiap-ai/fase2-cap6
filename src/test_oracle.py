from database import create_table, insert_data, fetch_data, get_unique_locations, delete_all_data
from datetime import datetime

def test_database_operations():
    print("Testing database operations:")
    
    create_table()
    
    insert_data("Test City", datetime.now(), 25.5, 10.2)
    
    data = fetch_data("Test City")
    print(f"Fetched data: {data}")
    
    locations = get_unique_locations()
    print(f"Unique locations: {locations}")
    
    delete_all_data()
    
    print("All tests completed.")

if __name__ == "__main__":
    test_database_operations()
