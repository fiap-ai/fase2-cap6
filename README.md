# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/gabemule/">Gabriel Mule Monteiro</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>


## 📜 Descrição

Este projeto consiste em um Sistema de Monitoramento Climático e Gestão de Riscos para o Agronegócio. O sistema foi desenvolvido para auxiliar agricultores e gestores do setor agrícola a tomar decisões informadas com base em dados climáticos precisos e análises preditivas.

O sistema oferece as seguintes funcionalidades principais:

1. Coleta de dados climáticos em tempo real de diversas fontes, incluindo estações meteorológicas e APIs de previsão do tempo.
2. Armazenamento eficiente dos dados coletados em um banco de dados Oracle.
3. Análise dos dados climáticos, incluindo cálculos de médias de temperatura, precipitação total e índices climáticos como o SPI (Standardized Precipitation Index).
4. Geração de alertas para condições climáticas extremas, como altas temperaturas ou precipitação excessiva.
5. Produção de relatórios detalhados sobre as condições climáticas de diferentes localidades.
6. Visualização dos dados através de gráficos e comparações entre diferentes cidades.
7. Análise de tendências climáticas usando médias móveis.
8. Exportação de dados para formatos facilmente manipuláveis, como CSV.

O sistema foi projetado com foco na usabilidade, permitindo que os usuários interajam com os dados de forma intuitiva através de um menu de opções. Além disso, o projeto foi desenvolvido com ênfase na modularidade e escalabilidade, permitindo fácil manutenção e adição de novas funcionalidades no futuro.

Este sistema tem o potencial de impactar significativamente o setor agrícola, fornecendo informações cruciais para o planejamento de plantio, irrigação, colheita e outras atividades agrícolas. Ao antecipar condições climáticas adversas, o sistema ajuda a mitigar riscos e otimizar a produção agrícola, contribuindo para a segurança alimentar e a eficiência do agronegócio.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: Contém imagens e outros recursos utilizados no projeto.

- <b>build</b>: Pasta onde são gerados os arquivos de saída do projeto, como relatórios e gráficos.

- <b>docs</b>: Documentação do projeto.

- <b>src</b>: Contém o código-fonte do projeto.
  - <b>climate_analysis.py</b>: Módulo para análise de dados climáticos.
  - <b>climate_data.py</b>: Módulo para gerenciamento de dados climáticos.
  - <b>config.py</b>: Configurações do projeto.
  - <b>database.py</b>: Módulo para interação com o banco de dados.
  - <b>db_config.py</b>: Configurações do banco de dados.
  - <b>main.py</b>: Arquivo principal do programa.
  - <b>weather_api.py</b>: Módulo para interação com a API de clima.

- <b>tests</b>: Contém os testes unitários e de integração do projeto.

- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### Pré-requisitos

Antes de executar o código, certifique-se de ter os seguintes componentes instalados em sua máquina:

1. Python 3.8 ou superior
2. pip (gerenciador de pacotes do Python)
3. Oracle Database 19c ou superior
4. Git (para clonar o repositório)

### Bibliotecas Python necessárias

O projeto utiliza as seguintes bibliotecas Python:

- cx_Oracle
- matplotlib
- numpy
- requests

Você pode instalar todas as bibliotecas necessárias usando o arquivo `requirements.txt` fornecido no projeto.

### Instalação e Configuração

1. Clone o repositório:
   ```
   git clone https://github.com/fiap-ai/fase2-cap6.git
   cd fase2-cap6
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione as seguintes variáveis:
     ```
     OPENWEATHERMAP_API_KEY=sua_chave_api_aqui
     ORACLE_USER=seu_usuario
     ORACLE_PASSWORD=sua_senha
     ORACLE_DSN=seu_dsn
     ORACLE_CLIENT_PATH=/path/to/oracle/instantclient
     ```

5. Configure o banco de dados Oracle:
   - Execute os scripts SQL fornecidos na pasta `docs` para criar as tabelas necessárias

### Execução

Para executar o programa principal:

1. Navegue até a pasta `src`:
   ```
   cd src
   ```

2. Execute o arquivo `main.py`:
   ```
   python main.py
   ```

3. Siga as instruções no menu interativo para utilizar as diferentes funcionalidades do sistema.

### Execução dos Testes

Para executar os testes unitários e de integração:

1. Navegue até a raiz do projeto
2. Execute o comando:
   ```
   python -m unittest discover -v tests
   ```

### Solução de Problemas

Se você encontrar problemas ao executar o código, verifique:

1. Se todas as dependências foram instaladas corretamente
2. Se as variáveis de ambiente estão configuradas corretamente
3. Se o banco de dados Oracle está acessível e configurado corretamente

Para mais informações ou se encontrar problemas persistentes, consulte a documentação na pasta `docs` ou entre em contato com a equipe de desenvolvimento.

## 🗃 Histórico de lançamentos

* 0.1.0 - 15/10/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">MODELO GIT FIAP por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
