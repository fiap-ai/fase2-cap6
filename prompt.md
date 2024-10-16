**Prompt para o Agente de Desenvolvimento:**

Você é um desenvolvedor experiente especializado em Python, gestão de projetos e agronegócio. Sua tarefa é executar todas as etapas do projeto descrito a seguir, seguindo estritamente as diretrizes e o escopo definidos. É crucial que todas as especificações sejam atendidas conforme descritas, pois quaisquer erros ou desvios poderão resultar em penalizações.

Por favor, siga as instruções passo a passo, utilizando as práticas de engenharia de prompt recomendadas, e assegure-se de que o projeto atenda aos objetivos propostos.

---

<Projeto>
  <Título>Sistema de Monitoramento e Gestão de Riscos Climáticos no Agronegócio</Título>
  <Descrição>
    Desenvolver um sistema em Python que permita aos produtores rurais monitorar, prever e gerenciar os riscos associados a secas e catástrofes naturais. O sistema deve auxiliar na tomada de decisão e na mitigação de impactos, contribuindo para a resiliência e sustentabilidade do setor agrícola.
  </Descrição>
  <Objetivos>
    <ObjetivoGeral>
      Criar uma solução tecnológica que utilize dados meteorológicos para prever riscos climáticos e fornecer recomendações aos produtores rurais.
    </ObjetivoGeral>
    <ObjetivosEspecíficos>
      <Objetivo>
        Integrar o sistema com APIs meteorológicas confiáveis para obter dados climáticos em tempo real e históricos.
      </Objetivo>
      <Objetivo>
        Implementar funcionalidades para análise de dados e cálculo de índices climáticos relevantes.
      </Objetivo>
      <Objetivo>
        Desenvolver um sistema de alertas e recomendações baseado em critérios definidos.
      </Objetivo>
      <Objetivo>
        Armazenar dados em um banco de dados Oracle, permitindo operações CRUD.
      </Objetivo>
      <Objetivo>
        Criar relatórios e visualizações claras, utilizando bibliotecas adequadas.
      </Objetivo>
      <Objetivo>
        Garantir uma interface de usuário amigável, validando rigorosamente os dados de entrada.
      </Objetivo>
    </ObjetivosEspecíficos>
  </Objetivos>
  <EspecificaçõesTécnicas>
    <ColetaDeDados>
      <Requisito>
        Integrar com APIs como OpenWeatherMap para obter dados climáticos.
      </Requisito>
      <Requisito>
        Permitir entrada manual de dados pelo usuário.
      </Requisito>
    </ColetaDeDados>
    <AnáliseDeDados>
      <Requisito>
        Calcular índices climáticos como o Índice de Precipitação e o SPI.
      </Requisito>
      <Requisito>
        Utilizar algoritmos estatísticos para prever tendências climáticas.
      </Requisito>
    </AnáliseDeDados>
    <SistemaDeAlertas>
      <Requisito>
        Definir limiares para emissão de alertas sobre eventos adversos.
      </Requisito>
      <Requisito>
        Gerar notificações e recomendações de ações para minimizar impactos.
      </Requisito>
    </SistemaDeAlertas>
    <ArmazenamentoDeDados>
      <Requisito>
        Utilizar banco de dados Oracle para armazenar dados e análises.
      </Requisito>
      <Requisito>
        Implementar operações CRUD para gerenciamento dos dados.
      </Requisito>
    </ArmazenamentoDeDados>
    <RelatóriosEVisualizações>
      <Requisito>
        Criar relatórios claros e gráficos informativos.
      </Requisito>
      <Requisito>
        Utilizar bibliotecas como matplotlib ou plotly.
      </Requisito>
    </RelatóriosEVisualizações>
    <UsabilidadeEInterface>
      <Requisito>
        Desenvolver interface de linha de comando amigável com menus claros.
      </Requisito>
      <Requisito>
        Validar rigorosamente os dados inseridos pelo usuário.
      </Requisito>
      <Requisito>
        Apresentar mensagens de erro e orientações de forma clara.
      </Requisito>
    </UsabilidadeEInterface>
    <EstruturasDeDadosETécnicasDeProgramação>
      <Requisito>
        Utilizar funções e procedimentos com passagem de parâmetros.
      </Requisito>
      <Requisito>
        Implementar listas, tuplas, dicionários e tabelas de memória.
      </Requisito>
      <Requisito>
        Manipular arquivos de texto e JSON para armazenamento e leitura.
      </Requisito>
    </EstruturasDeDadosETécnicasDeProgramação>
  </EspecificaçõesTécnicas>
  <PlanoDeExecução>
    <Fase name="Planejamento">
      <Passo>
        Definir requisitos funcionais e não funcionais detalhados.
      </Passo>
      <Passo>
        Analisar e selecionar APIs meteorológicas adequadas.
      </Passo>
      <Passo>
        Modelar o banco de dados Oracle, definindo tabelas e relacionamentos.
      </Passo>
    </Fase>
    <Fase name="Configuração do Ambiente">
      <Passo>
        Instalar um ENV em Python 3.x e bibliotecas necessárias (requests, cx_Oracle, matplotlib, pandas).
      </Passo>
      <Passo>
        Configurar acesso ao banco de dados Oracle.
      </Passo>
      <Passo>
        Obter chaves de API e testar conexão com as APIs selecionadas.
      </Passo>
    </Fase>
    <Fase name="Desenvolvimento">
      <Passo>
        Implementar módulo de coleta de dados (APIs e entrada manual).
      </Passo>
      <Passo>
        Desenvolver módulo de processamento e análise (cálculo de índices, previsões).
      </Passo>
      <Passo>
        Criar módulo de armazenamento de dados (operações CRUD no Oracle).
      </Passo>
      <Passo>
        Desenvolver interface de usuário amigável (linha de comando, menus).
      </Passo>
      <Passo>
        Implementar sistema de alertas e recomendações.
      </Passo>
      <Passo>
        Criar relatórios e visualizações (gráficos, exportação de dados).
      </Passo>
    </Fase>
    <Fase name="Testes e Validação">
      <Passo>
        Realizar testes unitários para funções e módulos.
      </Passo>
      <Passo>
        Executar testes de integração para verificar funcionamento conjunto.
      </Passo>
      <Passo>
        Validar usabilidade e ajustar interface conforme necessário.
      </Passo>
    </Fase>
    <Fase name="Documentação">
      <Passo>
        Documentar código com comentários e docstrings.
      </Passo>
      <Passo>
        Elaborar README detalhado com instruções de uso.
      </Passo>
      <Passo>
        Incluir informações sobre escopo e relevância do projeto.
      </Passo>
    </Fase>
    <Fase name="Entrega">
      <Passo>
        Verificar que todos os arquivos estão no repositório GitHub.
      </Passo>
      <Passo>
        Não alterar o código após a data de entrega.
      </Passo>
      <Passo>
        Seguir o template e diretrizes de versionamento fornecidos.
      </Passo>
    </Fase>
  </PlanoDeExecução>
  <DiretrizesImportantes>
    <Diretriz>
      Atender a todas as especificações técnicas e funcionais descritas.
    </Diretriz>
    <Diretriz>
      Garantir uso dos conteúdos estudados nos capítulos 3 a 6 sobre Python.
    </Diretriz>
    <Diretriz>
      Seguir boas práticas de programação e estilo de código.
    </Diretriz>
    <Diretriz>
      Implementar validação rigorosa dos dados de entrada.
    </Diretriz>
    <Diretriz>
      Apresentar dados de forma clara e organizada ao usuário.
    </Diretriz>
    <Diretriz>
      Buscar soluções inovadoras que agreguem valor ao projeto.
    </Diretriz>
    <Diretriz>
      Focar na relevância do sistema para produtores rurais e o agronegócio.
    </Diretriz>
  </DiretrizesImportantes>
  <ObservaçõesFinais>
    Utilize práticas de engenharia de prompt, incluindo o pensamento passo a passo (chain-of-thought), para garantir a execução correta das etapas. Caso encontre qualquer dúvida ou dificuldade, consulte as referências fornecidas ou busque orientação conforme necessário. A precisão e conformidade com as especificações são cruciais; erros ou desvios podem resultar em penalizações.
  </ObservaçõesFinais>
  <ReferênciasERecursos>
    <Referência>
      Práticas de Prompt Engineering:
      <Link>https://docs.anthropic.com/claude/docs/prompt-engineering-best-practices#be-clear-contextual-and-specific</Link>
      <Link>https://docs.anthropic.com/claude/docs/chain-of-thought</Link>
      <Link>https://docs.anthropic.com/claude/docs/use-xml-tags</Link>
      <Link>https://docs.anthropic.com/claude/docs/system-prompts</Link>
    </Referência>
    <Referência>
      Recursos Técnicos:
      <Link>APIs Meteorológicas: https://openweathermap.org/api</Link>
      <Link>Bibliotecas Python: requests, json, cx_Oracle, matplotlib, pandas</Link>
    </Referência>
    <Referência>
      Documentação do Projeto:
      Certifique-se de que o README inclua todas as informações necessárias, seguindo as diretrizes fornecidas.
    </Referência>
  </ReferênciasERecursos>
</Projeto>

---

**Instruções Adicionais:**

- **Seja Claro e Específico:** Certifique-se de compreender cada etapa antes de implementá-la. Se necessário, divida tarefas complexas em subtarefas menores.
- **Pense Passo a Passo:** Utilize o pensamento estruturado para planejar e executar cada fase do projeto.
- **Utilize Tags Estruturais:** As informações foram organizadas em tags XML para facilitar a compreensão e referência. Mantenha essa organização ao documentar seu progresso.
- **Mantenha a Comunicação:** Caso surjam dúvidas ou seja necessário esclarecer algum ponto, busque as informações nas referências ou consulte os responsáveis.

---

Por favor, inicie a execução do projeto seguindo as instruções acima, assegurando-se de cumprir todas as especificações e diretrizes. Sua atenção aos detalhes e aderência às especificações são essenciais para o sucesso deste projeto.