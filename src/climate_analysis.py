import statistics
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import csv
import os
import numpy as np

def get_temperature(entry):
    return entry[1] if isinstance(entry, tuple) else entry['temperature']

def get_precipitation(entry):
    return entry[2] if isinstance(entry, tuple) else entry['precipitation']

def get_date(entry):
    return entry[0] if isinstance(entry, tuple) else datetime.strptime(entry['date'] + ' ' + entry['time'], '%Y-%m-%d %I:%M:%S %p')

def calculate_average_temperature(data):
    temperatures = [get_temperature(entry) for entry in data]
    return statistics.mean(temperatures) if temperatures else None

def calculate_total_precipitation(data):
    return sum(get_precipitation(entry) for entry in data)

def calculate_spi(data, period=30):
    """
    Calcula um Índice de Precipitação Padronizado (SPI) simplificado.
    Este é um cálculo aproximado e não deve ser usado para análises reais.
    """
    precipitations = [get_precipitation(entry) for entry in data]
    if not precipitations:
        return 0
    
    mean = statistics.mean(precipitations)
    stdev = statistics.stdev(precipitations) if len(precipitations) > 1 else 0
    
    if stdev == 0:
        return 0  # Evita divisão por zero
    
    total_precip = sum(precipitations)
    return (total_precip - mean * period) / (stdev * (period ** 0.5))

def generate_alerts(data, temp_threshold=30, precip_threshold=50):
    alerts = []
    for entry in data:
        date_time = get_date(entry).strftime("%Y-%m-%d %I:%M:%S %p")
        temperature = get_temperature(entry)
        precipitation = get_precipitation(entry)
        if temperature > temp_threshold:
            alerts.append(f"Alerta de alta temperatura em {date_time}: {temperature:.1f}°C")
        if precipitation > precip_threshold:
            alerts.append(f"Alerta de alta precipitação em {date_time}: {precipitation:.1f}mm")
    return alerts

def generate_report(location, data, temp_threshold, precip_threshold):
    avg_temp = calculate_average_temperature(data)
    total_precip = calculate_total_precipitation(data)
    spi = calculate_spi(data)
    
    report = f"Relatório Climático para {location}\n"
    report += f"Período: {get_date(data[0]).strftime('%Y-%m-%d %I:%M:%S %p')} a {get_date(data[-1]).strftime('%Y-%m-%d %I:%M:%S %p')}\n"
    report += f"Temperatura média: {avg_temp:.1f}°C\n"
    report += f"Precipitação total: {total_precip:.1f}mm\n"
    report += f"SPI simplificado: {spi:.2f}\n"
    
    alerts = generate_alerts(data, temp_threshold, precip_threshold)
    if alerts:
        report += "\nAlertas:\n" + "\n".join(alerts)
    else:
        report += "\nNenhum alerta gerado para os limiares atuais."
    
    recommendations = generate_recommendations(alerts)
    report += "\n\nRecomendações:\n" + "\n".join(recommendations)
    
    return report

def plot_climate_data(location, data):
    dates = [get_date(entry) for entry in data]
    temperatures = [get_temperature(entry) for entry in data]
    precipitations = [get_precipitation(entry) for entry in data]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Dados Climáticos - {location}')

    ax1.plot(dates, temperatures, 'r-', marker='o')
    ax1.set_ylabel('Temperatura (°C)')
    ax1.set_title('Temperatura')
    ax1.grid(True)

    ax2.bar(dates, precipitations, color='b', alpha=0.7)
    ax2.set_ylabel('Precipitação (mm)')
    ax2.set_title('Precipitação')
    ax2.grid(True)

    plt.gcf().autofmt_xdate()
    
    os.makedirs('build', exist_ok=True)
    plt.savefig(f'build/{location}_climate_data.png')
    plt.close()

    print(f"Gráfico gerado para {location}")

def export_to_csv(location, data, filename):
    os.makedirs('build', exist_ok=True)
    full_path = os.path.join('build', filename)
    with open(full_path, 'w', newline='') as csvfile:
        fieldnames = ['date', 'temperature', 'precipitation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow({
                'date': get_date(entry).strftime("%Y-%m-%d %I:%M:%S %p"),
                'temperature': get_temperature(entry),
                'precipitation': get_precipitation(entry)
            })
    
    print(f"Dados exportados para {full_path}")

def compare_cities(cities_data):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('Comparação de Dados Climáticos entre Cidades')

    for city, data in cities_data.items():
        dates = [get_date(entry) for entry in data]
        temperatures = [get_temperature(entry) for entry in data]
        precipitations = [get_precipitation(entry) for entry in data]

        ax1.plot(dates, temperatures, label=city)
        ax2.plot(dates, precipitations, label=city)

    ax1.set_ylabel('Temperatura (°C)')
    ax1.set_title('Comparação de Temperaturas')
    ax1.legend()
    ax1.grid(True)

    ax2.set_ylabel('Precipitação (mm)')
    ax2.set_title('Comparação de Precipitações')
    ax2.legend()
    ax2.grid(True)

    plt.gcf().autofmt_xdate()

    os.makedirs('build', exist_ok=True)
    plt.savefig('build/cities_comparison.png')
    plt.close()

    print("Gráfico de comparação gerado: build/cities_comparison.png")

def generate_comparison_report(cities_data, temp_threshold, precip_threshold):
    report = "Relatório Comparativo entre Cidades\n\n"
    
    for city, data in cities_data.items():
        avg_temp = calculate_average_temperature(data)
        total_precip = calculate_total_precipitation(data)
        spi = calculate_spi(data)
        
        report += f"{city}:\n"
        report += f"  Período: {get_date(data[0]).strftime('%Y-%m-%d %I:%M:%S %p')} a {get_date(data[-1]).strftime('%Y-%m-%d %I:%M:%S %p')}\n"
        report += f"  Temperatura média: {avg_temp:.1f}°C\n"
        report += f"  Precipitação total: {total_precip:.1f}mm\n"
        report += f"  SPI simplificado: {spi:.2f}\n"
        
        alerts = generate_alerts(data, temp_threshold, precip_threshold)
        if alerts:
            report += "  Alertas:\n    " + "\n    ".join(alerts) + "\n"
        else:
            report += "  Nenhum alerta gerado para os limiares atuais.\n"
        
        report += "\n"
    
    return report

def plot_moving_average(location, data, window):
    dates = [get_date(entry) for entry in data]
    temperatures = [get_temperature(entry) for entry in data]
    precipitations = [get_precipitation(entry) for entry in data]

    temp_ma = np.convolve(temperatures, np.ones(window), 'valid') / window
    precip_ma = np.convolve(precipitations, np.ones(window), 'valid') / window
    dates_ma = dates[window-1:]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Média Móvel de {window} dias - {location}')

    ax1.plot(dates, temperatures, 'r-', alpha=0.5, label='Dados Originais')
    ax1.plot(dates_ma, temp_ma, 'b-', label='Média Móvel')
    ax1.set_ylabel('Temperatura (°C)')
    ax1.set_title('Média Móvel de Temperatura')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(dates, precipitations, 'r-', alpha=0.5, label='Dados Originais')
    ax2.plot(dates_ma, precip_ma, 'b-', label='Média Móvel')
    ax2.set_ylabel('Precipitação (mm)')
    ax2.set_title('Média Móvel de Precipitação')
    ax2.legend()
    ax2.grid(True)

    plt.gcf().autofmt_xdate()

    os.makedirs('build', exist_ok=True)
    plt.savefig(f'build/{location}_moving_average.png')
    plt.close()

    print(f"Gráfico de média móvel gerado: build/{location}_moving_average.png")

def generate_recommendations(alerts):
    recommendations = []
    high_temp_count = sum(1 for alert in alerts if "alta temperatura" in alert)
    high_precip_count = sum(1 for alert in alerts if "alta precipitação" in alert)

    if high_temp_count > 0:
        recommendations.append(f"Devido a {high_temp_count} alerta(s) de alta temperatura:")
        recommendations.append("- Aumente a frequência de irrigação")
        recommendations.append("- Considere o uso de coberturas para proteger as culturas sensíveis")
        recommendations.append("- Monitore sinais de estresse térmico nas plantas")

    if high_precip_count > 0:
        recommendations.append(f"Devido a {high_precip_count} alerta(s) de alta precipitação:")
        recommendations.append("- Verifique e melhore a drenagem do solo")
        recommendations.append("- Considere o uso de culturas de cobertura para prevenir erosão")
        recommendations.append("- Monitore sinais de doenças fúngicas nas plantas")

    if not recommendations:
        recommendations.append("Não há recomendações específicas baseadas nos alertas atuais.")

    return recommendations
