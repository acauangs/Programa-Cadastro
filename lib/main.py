from lib.interface import *
from lib.arquivo import *
from time import sleep
arq = 'pessoas.txt'

if not arquivo_yes(arq):
    criar_arq(arq)


while True:
    opc = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair'])
    if opc == 1:
        ler_arquivo(arq)
    elif opc == 2:
        cabeçalho('CASDASTRAR UMA NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opc == 3:
        linha()
        print('Programa Encerrado \nVolte Sempre!')
        linha()
        break
    else:
        print('\033[31mERRO, por favor digite um númeiro inteiro válido.\033[m')
        sleep(2)
