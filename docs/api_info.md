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

## Limites de Chamadas:
- Plano Gratuito: 60 chamadas por minuto, 1,000,000 por mês
- Planos Pagos: Variam de acordo com o nível de assinatura

## Dados Fornecidos:
- Temperatura
- Umidade
- Pressão Atmosférica
- Velocidade do Vento
- Direção do Vento
- Precipitação
- Cobertura de Nuvens

## Observações:
- É necessário se registrar para obter uma chave de API
- Dados históricos detalhados requerem uma assinatura paga
- A API fornece dados em formato JSON, facilitando a integração com Python

## Próximos Passos:
1. Registrar-se no OpenWeatherMap para obter uma chave de API
2. Implementar funções para fazer chamadas à API usando a biblioteca requests
3. Desenvolver funções para processar e armazenar os dados recebidos
