# Comandos do Sistema de Monitoramento Climático

Este documento lista os principais comandos que podem ser executados via linha de comando no nosso projeto de monitoramento climático.

## Comando Principal

Para rodar nossa ferramenta CLI principal:

```
python src/main.py
```

Este comando inicia a interface de linha de comando interativa do nosso sistema de monitoramento climático.

## Comandos de Teste

Para executar os testes do nosso projeto, você pode usar os seguintes comandos:

1. Teste do sistema climático:
```
python src/test_climate_system.py
```

2. Teste das operações CRUD no Oracle:
```
python src/test_oracle_crud.py
```

3. Teste da conexão com o Oracle:
```
python src/test_oracle.py
```

Estes comandos executam os testes correspondentes e fornecem feedback sobre o funcionamento das diferentes partes do nosso sistema.

4. Teste da API de clima:
```
python src/weather_api.py
```

Este comando executa um teste da API de clima, buscando dados meteorológicos para o Rio de Janeiro, Brasil.

5. Inicialização do banco de dados:
```
python src/database.py
```

Este comando cria a tabela necessária no banco de dados Oracle. Observe que esta operação é executada automaticamente quando o arquivo é importado, então normalmente não é necessário executá-lo diretamente.
