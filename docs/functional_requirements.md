# Requisitos Funcionais

1. Coleta de Dados Meteorológicos:
   - Integração com API OpenWeatherMap para obtenção de dados em tempo real e previsões
   - Capacidade de buscar dados para múltiplas cidades

2. Análise de Riscos Climáticos:
   - Cálculo do Índice de Precipitação
   - Cálculo do SPI (Standardized Precipitation Index)
   - Análise de tendências climáticas usando médias móveis

3. Sistema de Alertas e Recomendações:
   - Definição de limiares para emissão de alertas de temperatura e precipitação
   - Geração de alertas sobre eventos climáticos adversos
   - Sugestões de ações para minimizar impactos nas culturas agrícolas

4. Armazenamento de Dados:
   - Persistência de dados meteorológicos em banco Oracle
   - Implementação de operações CRUD (Create, Read, Update, Delete)
   - Capacidade de limpar todos os dados armazenados

5. Relatórios e Visualizações:
   - Geração de relatórios climáticos detalhados
   - Criação de gráficos para visualização de dados de temperatura e precipitação
   - Geração de gráficos comparativos entre diferentes cidades
   - Exportação de dados para formato CSV

6. Interface de Usuário:
   - Menu interativo via linha de comando
   - Opções para visualizar dados, gerar relatórios e gráficos
   - Capacidade de configurar limiares de alerta

7. Análise Comparativa:
   - Comparação de dados climáticos entre diferentes cidades
   - Visualização de períodos específicos de dados

8. Desempenho:
   - Capacidade de processar e analisar grandes volumes de dados climáticos
   - Otimização de consultas ao banco de dados para rápida recuperação de informações

9. Flexibilidade:
   - Capacidade de adicionar novas cidades para monitoramento
   - Possibilidade de estender o sistema para incluir novos tipos de análises no futuro

10. Testes:
    - Conjunto abrangente de testes unitários e de integração
    - Testes de desempenho para garantir a eficiência do sistema
