# projeto-lista-todo
Projeto de lista de tarefas desenvolvido em Python com foco em prática de lógica de programação, manipulação de dados e persistência em arquivos.

Funcionalidades:
-Adicionar tarefas
-Listar tarefas com índice
-Remover tarefas
-Marcar tarefas como concluídas
-Persistência de dados utilizando JSON

Conceitos aplicados
-Estruturas de dados (listas e dicionários)
-Funções (def) para organização do código
-Laços de repetição (while, for)
-Condicionais (if, else)
-Tratamento de exceções (try/except)
-Manipulação de arquivos (open, modos "r" e "w")
-Serialização de dados com JSON (json.load e json.dump)

Como funciona o armazenamento:
As tarefas são armazenadas em um arquivo agenda.json, permitindo que os dados sejam mantidos mesmo após o encerramento do programa.
Exemplo de estrutura:

[
  {
    "nome": "Estudar Python",
    "feito": false
  }
]

Melhorias futuras:
-Adição de data e hora nas tarefas
-Sistema de login por usuário
-Interface gráfica
-Integração com banco de dados

Aprendizados adquiridos:
Este projeto foi desenvolvido com o objetivo de consolidar conceitos fundamentais de programação em Python, especialmente no gerenciamento de dados e construção de aplicações interativas em terminal.
