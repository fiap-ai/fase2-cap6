# API OpenWeatherMap

URL Base: https://api.openweathermap.org/data/2.5/

## Endpoints Relevantes:
1. Clima Atual: /weather
2. Previsão de 5 dias: /forecast
3. Dados Históricos: /onecall/timemachine (requer assinatura)

## Parâmetros Comuns:
- lat: latitude
- lon: longitude
- appid: chave da API
- units: unidades de medida (metric para Celsius)
- lang: idioma (pt_br para português)

## Limites de Chamadas:
- Plano Gratuito: 60 chamadas por minuto, 1,000,000 por mês
- Planos Pagos: Variam de acordo com o nível de assinatura

## Dados Fornecidos:
- Temperatura (atual, mínima, máxima)
- Umidade
- Pressão Atmosférica
- Velocidade do Vento
- Direção do Vento
- Precipitação
- Cobertura de Nuvens
- Descrição do clima

## Observações:
- É necessário se registrar para obter uma chave de API
- Dados históricos detalhados requerem uma assinatura paga
- A API fornece dados em formato JSON, facilitando a integração com Python
- As respostas da API incluem códigos de condição climática que podem ser úteis para análises mais detalhadas

## Implementação no Projeto:
1. A chave da API é armazenada como uma variável de ambiente (OPENWEATHERMAP_API_KEY)
2. O módulo weather_api.py contém funções para interagir com a API:
   - get_coordinates(): obtém as coordenadas de uma cidade
   - fetch_weather_data(): busca dados climáticos atuais e previsões
3. Os dados obtidos são processados e armazenados no banco de dados Oracle para análises posteriores

## Próximos Passos:
1. Considerar a implementação de cache para reduzir o número de chamadas à API
2. Explorar a possibilidade de usar dados históricos para análises mais profundas (requer upgrade do plano)
3. Implementar tratamento de erros mais robusto para lidar com falhas na API ou limites de taxa excedidos
