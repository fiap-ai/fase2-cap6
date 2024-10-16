from datetime import datetime
from database import insert_data, fetch_data, delete_all_data, get_unique_locations, update_data, delete_data
import traceback
import sys

class ClimateData:
    def __init__(self):
        self.data = {}
        self.load_data_from_database()

    def load_data_from_database(self):
        locations = get_unique_locations()
        for location in locations:
            db_data = fetch_data(location)
            self.data[location] = [
                {
                    'date': entry[0].strftime("%Y-%m-%d"),
                    'time': entry[0].strftime("%I:%M:%S %p"),
                    'temperature': entry[1],
                    'precipitation': entry[2]
                }
                for entry in db_data
            ]

    def add_data(self, location, temperature, precipitation, date=None, time=None):
        if not isinstance(temperature, (int, float)) or not isinstance(precipitation, (int, float)):
            raise ValueError("Temperature and precipitation must be numbers")

        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        if time is None:
            time = datetime.now().strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
        
        date_time = f"{date} {time}"
        try:
            oracle_date = datetime.strptime(date_time, "%Y-%m-%d %I:%M:%S %p").strftime("%d-%b-%Y %I:%M:%S %p")
            insert_data(location, oracle_date, temperature, precipitation)
            
            if location not in self.data:
                self.data[location] = []
            self.data[location].append({
                'date': date,
                'time': time,
                'temperature': temperature,
                'precipitation': precipitation
            })
        except Exception as e:
            print(f"Error inserting data: {e}")
            print(traceback.format_exc())

    def update_data(self, location, date, time, temperature, precipitation):
        try:
            date_time = f"{date} {time}"
            oracle_date = datetime.strptime(date_time, "%Y-%m-%d %I:%M:%S %p").strftime("%d-%b-%Y %I:%M:%S %p")
            update_data(location, oracle_date, temperature, precipitation)
            
            if location in self.data:
                for entry in self.data[location]:
                    if entry['date'] == date and entry['time'] == time:
                        entry['temperature'] = temperature
                        entry['precipitation'] = precipitation
                        break
            else:
                print(f"Location '{location}' not found in local data. Updating only in database.")
        except Exception as e:
            print(f"Error updating data: {e}")
            print(traceback.format_exc())

    def delete_data(self, location, date, time):
        try:
            date_time = f"{date} {time}"
            oracle_date = datetime.strptime(date_time, "%Y-%m-%d %I:%M:%S %p").strftime("%d-%b-%Y %I:%M:%S %p")
            delete_data(location, oracle_date)
            
            if location in self.data:
                self.data[location] = [entry for entry in self.data[location] if not (entry['date'] == date and entry['time'] == time)]
        except Exception as e:
            print(f"Error deleting data: {e}")
            print(traceback.format_exc())

    def add_real_data(self, location, data):
        try:
            if 'daily' not in data:
                print("Error: 'daily' key not found in data")
                return
            
            for entry in data['daily']:
                date = entry['date']
                temperature = entry['temperature']
                precipitation = entry['precipitation']
                time = "12:00:00 PM"  # Set a default time for daily data
                self.add_data(location, temperature, precipitation, date, time)
            
            print(f"Dados reais para {location} adicionados com sucesso (previsão para {len(data['daily'])} dias, limitado pela API gratuita).")
        except Exception as e:
            print(f"Critical error in add_real_data: {e}")
            print(traceback.format_exc())

    def get_data(self, location, start_date=None, end_date=None):
        if location not in self.data:
            db_data = fetch_data(location)
            self.data[location] = [
                {
                    'date': entry[0].strftime("%Y-%m-%d"),
                    'time': entry[0].strftime("%I:%M:%S %p"),
                    'temperature': entry[1],
                    'precipitation': entry[2]
                }
                for entry in db_data
            ]
        
        data = self.data.get(location, [])
        
        if not data:
            return []

        if start_date is None and end_date is None:
            return sorted(data, key=lambda x: x['date'])
        
        filtered_data = []
        for entry in data:
            entry_date = datetime.strptime(entry['date'], "%Y-%m-%d").date()
            if (start_date is None or entry_date >= start_date) and (end_date is None or entry_date <= end_date):
                filtered_data.append(entry)
        
        return sorted(filtered_data, key=lambda x: x['date'])

    def get_all_locations(self):
        return list(self.data.keys())

    def clear_data(self):
        delete_all_data()
        self.data = {}
        print("Todos os dados climáticos foram limpos.")
