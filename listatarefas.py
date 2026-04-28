import json

def listar(agenda):
   print('------LISTA-------')
   if not agenda:
            print('Lista vazia')
            return
   
   for i, tarefa in enumerate(agenda):
        if tarefa["feito"]:
            status = 'X'
        else:
            status = ' '
        print(f'[{i}] {tarefa["nome"]} [{status}]')

try:
    with open("agenda.json", "r") as arquivo:
        agenda = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    agenda = []

def salvar(agenda):
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo)

while True:
  print('======MENU=======')
  print('[1] ADICIONAR')
  print('[2] LISTAR ITENS')
  print('[3] REMOVER')
  print('[4] MARCAR COMO CONCLUIDO')
  print('[0] SAIR')
  try:
      funcao = int(input('INSIRA QUAL FUNÇÃO DESEJA REALIZAR: '))
      match funcao:
        case 1:
          afazer = input('Adicione um afazer ')
          agenda.append({'nome':afazer, 'feito': False})
          print('Adicionado com sucesso! ')
          salvar(agenda)
        case 2:
            listar(agenda)

        case 3:
          listar(agenda)
          remover = int(input('Qual deseja remover?: '))
          if 0<= remover< len(agenda):
                agenda.pop(remover)
                print('Removido com sucesso! ')
                salvar(agenda)
          else:
                print(f'Insira um número entre 0 e {len(agenda) - 1}')
          listar(agenda)

        case 4:
            listar(agenda)
            concluido = int(input('Qual deseja marcar como concluido?: '))
            if 0<= concluido < len(agenda):
                   agenda[concluido]["feito"] = True
                   print('Marcado com sucesso! ')
                   salvar(agenda)
            else:
                print(f'Insira um número entre 0 e {len(agenda) - 1}')
            listar(agenda)

        case 0:
            print('Saindo...')
            break
          
        case _:
            print('INVÁLIDO, INSIRA SOMENTE NÚMEROS INTEIROS DE 0 A 4')

  except ValueError:
      print('INVÁLIDO, INSIRA SOMENTE MÚMEROS INTEIROS DE 0 A 4')
  continuar = input('DESEJA REALIZAR MAIS FUNÇÕES? ')
  if continuar.lower() != 's' and continuar.lower() != 'sim':
     break
  else:
      continue