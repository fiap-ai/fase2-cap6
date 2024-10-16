# Sistema de Monitoramento e Gestão de Riscos Climáticos no Agronegócio

## Visão Geral

Este projeto implementa um sistema de monitoramento e gestão de riscos climáticos voltado especificamente para o setor do agronegócio. O sistema foi desenvolvido para atender às necessidades únicas dos produtores rurais, focando em como as mudanças climáticas e eventos meteorológicos extremos podem afetar a produção agrícola.

### Relevância para o Agronegócio

O agronegócio é um setor crucial para a economia global e particularmente importante no Brasil. No entanto, é também um dos setores mais vulneráveis às mudanças climáticas. Este sistema aborda diretamente os seguintes aspectos do agronegócio:

1. **Gestão de Riscos Climáticos**: Auxilia os produtores a antecipar e se preparar para eventos climáticos adversos que podem afetar as safras.
2. **Planejamento de Safra**: Fornece dados climáticos históricos e previsões que podem ajudar no planejamento do plantio e colheita.
3. **Irrigação Eficiente**: As informações sobre precipitação e temperatura ajudam a otimizar os sistemas de irrigação.
4. **Controle de Pragas e Doenças**: Mudanças climáticas podem influenciar a proliferação de pragas e doenças. O sistema ajuda a prever condições favoráveis a esses problemas.
5. **Sustentabilidade**: Ao fornecer dados precisos, o sistema contribui para práticas agrícolas mais sustentáveis e eficientes no uso de recursos.

## Impacto no Agronegócio

Este sistema tem o potencial de transformar a maneira como os produtores rurais tomam decisões baseadas em dados climáticos. Ao fornecer informações precisas e análises detalhadas, o sistema pode ajudar a:

1. Reduzir perdas de safra devido a eventos climáticos extremos
2. Otimizar o uso de recursos hídricos e energéticos
3. Melhorar o planejamento de plantio e colheita
4. Aumentar a produtividade geral das operações agrícolas
5. Promover práticas agrícolas mais sustentáveis e resilientes às mudanças climáticas

Ao adotar este sistema, os produtores rurais estarão melhor equipados para enfrentar os desafios climáticos do século 21, contribuindo para um setor de agronegócio mais forte e sustentável.

## Funcionalidades Principais

1. **Coleta de Dados Climáticos**: Integração com APIs meteorológicas para obtenção de dados em tempo real, cruciais para decisões diárias no campo.
2. **Análise de Riscos**: Cálculo de índices climáticos relevantes para a agricultura, como o Índice de Precipitação Padronizado (SPI).
3. **Geração de Alertas**: Notificações sobre possíveis eventos climáticos adversos que podem afetar as culturas.
4. **Recomendações Agrícolas**: Sugestões de ações para minimizar impactos negativos nas safras, baseadas nas condições climáticas previstas.
5. **Visualização de Dados**: Geração de gráficos e relatórios para fácil interpretação das condições climáticas e seus potenciais impactos na produção.
6. **Comparação entre Regiões**: Análise comparativa de dados climáticos de diferentes localidades, útil para decisões de expansão ou diversificação de culturas.
7. **Análise de Tendências**: Cálculo de médias móveis para identificação de padrões climáticos de longo prazo que podem afetar o planejamento agrícola.
8. **Exportação de Dados**: Possibilidade de exportar dados para formato CSV, facilitando a integração com outros sistemas de gestão agrícola.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.8 ou superior
- **Banco de Dados**: Oracle 19c ou superior
- **Bibliotecas Principais**:
  - `requests`: Para chamadas à API meteorológica
  - `cx_Oracle`: Para conexão com o banco de dados Oracle
  - `matplotlib`: Para geração de gráficos relevantes para análise agrícola
  - `numpy`: Para cálculos e análises numéricas

## Estrutura do Projeto

```
.
├── src/
│   ├── main.py              # Ponto de entrada do programa
│   ├── climate_data.py      # Classe para manipulação de dados climáticos
│   ├── climate_analysis.py  # Funções para análise de dados climáticos relevantes para agricultura
│   ├── database.py          # Funções para interação com o banco de dados
│   ├── weather_api.py       # Funções para interação com a API meteorológica
│   ├── config.py            # Configurações do sistema
│   └── db_config.py         # Configurações do banco de dados
├── docs/
│   ├── README.md            # Documentação detalhada do projeto
│   ├── api_info.md          # Informações sobre a API de clima utilizada
│   ├── commands.md          # Lista de comandos úteis
│   ├── functional_requirements.md  # Requisitos funcionais do sistema
│   └── non_functional_requirements.md  # Requisitos não funcionais do sistema
├── build/                   # Pasta para armazenar gráficos e arquivos gerados
├── tests/                   # Pasta para testes unitários e de integração
├── .env                     # Arquivo para armazenar variáveis de ambiente (não versionado)
├── .gitignore               # Arquivo para especificar arquivos/pastas ignorados pelo Git
├── requirements.txt         # Lista de dependências do projeto
└── README.md                # README principal do repositório
```

## Configuração e Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/fiap-ai/fase2-cap6.git
   cd fase2-cap6
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:
   ```
   OPENWEATHERMAP_API_KEY=sua_chave_api
   ORACLE_USER=seu_usuario_oracle
   ORACLE_PASSWORD=sua_senha_oracle
   ORACLE_DSN=seu_dsn_oracle
   ORACLE_CLIENT_PATH=/path/to/oracle/instantclient
   ```

4. Execute o programa principal:
   ```
   python src/main.py
   ```

## Uso do Sistema

Ao executar o programa, um menu interativo será apresentado com as seguintes opções:

1. Buscar dados reais
2. Ver e exportar relatório climático
3. Gerar gráfico de dados climáticos
4. Configurar limiares de alerta
5. Exportar dados para CSV
6. Comparar cidades
7. Visualizar período específico
8. Analisar tendências (média móvel)
9. Limpar todos os dados
10. Sair

Siga as instruções na tela para navegar e utilizar as funcionalidades do sistema.
