# Comandos do Sistema de Monitoramento Climático

Este documento lista os principais comandos que podem ser executados via linha de comando no nosso projeto de monitoramento climático.

## Comando Principal

Para rodar nossa ferramenta CLI principal:

```
python src/main.py
```

Este comando inicia a interface de linha de comando interativa do nosso sistema de monitoramento climático.

## Comandos de Teste

Para executar todos os testes do projeto de uma vez:

```
python -m unittest discover -v tests
```

Este comando executará todos os testes unitários e de integração localizados na pasta 'tests'.

Para executar testes específicos, você pode usar os seguintes comandos:

1. Teste do sistema climático:
```
python -m unittest tests.test_climate_system
```

2. Teste das operações CRUD no Oracle:
```
python -m unittest tests.test_oracle_crud
```

3. Teste da conexão com o Oracle:
```
python -m unittest tests.test_oracle
```

4. Teste da API de clima:
```
python -m unittest tests.test_weather_api
```

5. Testes de desempenho:
```
python -m unittest tests.test_performance
```

Estes comandos executam os testes correspondentes e fornecem feedback sobre o funcionamento das diferentes partes do nosso sistema.

## Outros Comandos Úteis

1. Instalação de dependências:
```
pip install -r requirements.txt
```

2. Limpeza da pasta de build:
```
python src/main.py
```
Selecione a opção 9 no menu interativo para limpar todos os dados e arquivos gerados.

3. Exportação de dados para CSV:
```
python src/main.py
```
Selecione a opção 5 no menu interativo para exportar dados para CSV.

Lembre-se de que para executar qualquer comando, você deve estar no diretório raiz do projeto e ter o ambiente virtual ativado (se estiver usando um).
