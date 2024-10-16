from climate_data import ClimateData
from datetime import datetime, timedelta

def test_oracle_crud():
    climate_data = ClimateData()
    
    # Criar um item
    location = "Test City"
    date = datetime.now().strftime("%Y-%m-%d")
    time = "12:00:00 PM"
    temperature = 25.5
    precipitation = 10.2
    
    print("1. Criando um novo item:")
    climate_data.add_data(location, temperature, precipitation, date, time)
    
    # Mostrar o item
    print("\n2. Mostrando o item criado:")
    data = climate_data.get_data(location)
    print(data)
    
    # Atualizar o item
    new_temperature = 26.0
    new_precipitation = 15.5
    print("\n3. Atualizando o item:")
    climate_data.update_data(location, date, time, new_temperature, new_precipitation)
    
    # Mostrar o item atualizado
    print("\n4. Mostrando o item atualizado:")
    data = climate_data.get_data(location)
    print(data)
    
    # Remover o item
    print("\n5. Removendo o item:")
    climate_data.delete_data(location, date, time)
    
    # Tentar mostrar o item removido
    print("\n6. Tentando mostrar o item removido:")
    data = climate_data.get_data(location)
    print(data)

if __name__ == "__main__":
    test_oracle_crud()
