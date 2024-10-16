from climate_data import ClimateData
from climate_analysis import generate_report, plot_climate_data, export_to_csv, compare_cities, generate_comparison_report, plot_moving_average
from config import get_thresholds, set_thresholds
from datetime import datetime, timedelta
from weather_api import fetch_weather_data
import os
import glob
import shutil
import traceback
import sys

def clear_build_folder():
    build_path = os.path.join(os.path.dirname(__file__), '..', 'build')
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
    os.makedirs(build_path)
    print("Build folder cleared and recreated.")

def print_menu():
    print("\n1. Buscar dados reais")
    print("2. Ver relatório climático")
    print("3. Gerar gráfico de dados climáticos")
    print("4. Configurar limiares de alerta")
    print("5. Exportar dados para CSV")
    print("6. Comparar cidades")
    print("7. Visualizar período específico")
    print("8. Analisar tendências (média móvel)")
    print("9. Limpar todos os dados")
    print("10. Sair")

def get_date_input(prompt, min_date, max_date):
    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD) [intervalo: {min_date} a {max_date}]: ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if min_date <= date <= max_date:
                return date
            else:
                print(f"Data fora do intervalo. Por favor, escolha uma data entre {min_date} e {max_date}.")
        except ValueError:
            print("Formato de data inválido. Use YYYY-MM-DD.")

def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def main():
    try:
        clear_build_folder()
        climate_data = ClimateData()
        temp_threshold, precip_threshold = get_thresholds()

        if not os.environ.get("OPENWEATHERMAP_API_KEY"):
            print("Aviso: A chave da API OpenWeatherMap não está configurada.")
            print("Configure a variável de ambiente OPENWEATHERMAP_API_KEY para usar dados reais.")

        while True:
            print_menu()
            choice = input("Escolha uma opção: ")

            if choice == '1':
                city = input("Digite o nome da cidade: ")
                country_code = input("Digite o código do país (ex: BR para Brasil): ")
                print(f"Buscando dados para {city}, {country_code}...")
                data = fetch_weather_data(city, country_code)
                if data and 'daily' in data:
                    print("Dados obtidos com sucesso. Adicionando ao sistema...")
                    climate_data.add_real_data(city, data)
                    print("Dados adicionados com sucesso.")
                else:
                    print("Falha ao buscar dados reais ou dados inválidos recebidos.")

            elif choice == '2':
                locations = climate_data.get_all_locations()
                if not locations:
                    print("Nenhum dado climático disponível. Por favor, busque dados reais primeiro.")
                else:
                    for location in locations:
                        print(f"Gerando relatório para {location}...")
                        data = climate_data.get_data(location)
                        if data:
                            report = generate_report(location, data, temp_threshold, precip_threshold)
                            print(report)
                            print("-" * 50)
                        else:
                            print(f"Sem dados para {location}")

            elif choice == '3':
                locations = climate_data.get_all_locations()
                if not locations:
                    print("Nenhum dado climático disponível. Por favor, busque dados reais primeiro.")
                else:
                    for location in locations:
                        data = climate_data.get_data(location)
                        if data:
                            file_path = f'build/{location}_climate_data.png'
                            delete_file_if_exists(file_path)
                            plot_climate_data(location, data)
                            print(f"Gráfico gerado para {location}")
                        else:
                            print(f"Sem dados para gerar gráfico de {location}")

            elif choice == '4':
                try:
                    temp_threshold = float(input(f"Digite o novo limiar de temperatura para alertas (°C) [atual: {temp_threshold}]: "))
                    precip_threshold = float(input(f"Digite o novo limiar de precipitação para alertas (mm) [atual: {precip_threshold}]: "))
                    set_thresholds(temp_threshold, precip_threshold)
                    print(f"Novos limiares configurados: Temperatura > {temp_threshold}°C, Precipitação > {precip_threshold}mm")
                except ValueError:
                    print("Entrada inválida. Por favor, insira números válidos.")

            elif choice == '5':
                locations = climate_data.get_all_locations()
                if not locations:
                    print("Nenhum dado climático disponível. Por favor, busque dados reais primeiro.")
                else:
                    for location in locations:
                        data = climate_data.get_data(location)
                        if data:
                            filename = f"{location.lower().replace(' ', '_')}_climate_data.csv"
                            file_path = f'build/{filename}'
                            delete_file_if_exists(file_path)
                            export_to_csv(location, data, filename)
                        else:
                            print(f"Sem dados para exportar de {location}")

            elif choice == '6':
                cities_data = {}
                locations = climate_data.get_all_locations()
                if not locations:
                    print("Nenhum dado climático disponível. Por favor, busque dados reais primeiro.")
                else:
                    for location in locations:
                        data = climate_data.get_data(location)
                        if data:
                            cities_data[location] = data
                    
                    if cities_data:
                        file_path = 'build/cities_comparison.png'
                        delete_file_if_exists(file_path)
                        compare_cities(cities_data)
                        comparison_report = generate_comparison_report(cities_data, temp_threshold, precip_threshold)
                        print(comparison_report)
                    else:
                        print("Sem dados suficientes para comparar cidades.")

            elif choice == '7':
                locations = climate_data.get_all_locations()
                if not locations:
                    print("Nenhum dado climático disponível. Por favor, busque dados reais primeiro.")
                else:
                    location = input("Digite o nome da cidade: ")
                    if location in locations:
                        data = climate_data.get_data(location)
                        if data:
                            min_date = datetime.strptime(data[0]['date'], "%Y-%m-%d").date()
                            max_date = datetime.strptime(data[-1]['date'], "%Y-%m-%d").date()
                            start_date = get_date_input("Digite a data de início", min_date, max_date)
                            end_date = get_date_input("Digite a data de fim", start_date, max_date)
                            filtered_data = climate_data.get_data(location, start_date, end_date)
                            if filtered_data:
                                report = generate_report(location, filtered_data, temp_threshold, precip_threshold)
                                print(report)
                                file_path = f'build/{location}_{start_date}_{end_date}_climate_data.png'
                                delete_file_if_exists(file_path)
                                plot_climate_data(f"{location}_{start_date}_{end_date}", filtered_data)
                                print(f"Gráfico gerado para {location} no período especificado")
                            else:
                                print(f"Sem dados para {location} no período especificado")
                        else:
                            print(f"Sem dados disponíveis para {location}")
                    else:
                        print("Cidade não encontrada.")

            elif choice == '8':
                locations = climate_data.get_all_locations()
                if not locations:
                    print("Nenhum dado climático disponível. Por favor, busque dados reais primeiro.")
                else:
                    location = input("Digite o nome da cidade para análise de tendências: ")
                    if location in locations:
                        data = climate_data.get_data(location)
                        if data:
                            while True:
                                try:
                                    window = int(input(f"Digite o número de dias para a média móvel (máximo {len(data)}): "))
                                    if 1 <= window <= len(data):
                                        break
                                    else:
                                        print(f"Por favor, insira um número entre 1 e {len(data)}.")
                                except ValueError:
                                    print("Por favor, insira um número inteiro válido.")
                            file_path = f'build/{location}_moving_average.png'
                            delete_file_if_exists(file_path)
                            plot_moving_average(location, data, window)
                        else:
                            print(f"Sem dados para analisar tendências de {location}")
                    else:
                        print("Cidade não encontrada.")

            elif choice == '9':
                confirm = input("Tem certeza que deseja limpar todos os dados? (s/n): ")
                if confirm.lower() == 's':
                    climate_data.clear_data()
                    clear_build_folder()
                    print("Todos os dados e arquivos gerados foram limpos.")
                else:
                    print("Operação cancelada.")

            elif choice == '10':
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida. Por favor, tente novamente.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
