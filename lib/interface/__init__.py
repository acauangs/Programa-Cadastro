from lib.arquivo import *

def leiaInt(msg):
    """
    Funcao para validar a entrada de um numero do tipo inteiro
    """
    while True:
        try:
            num = int(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[31mERRO, por favor digite um númeiro inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('Usuário preferio não informar nenhum valor')


def linha(tam = 42):
    print('-' * tam)


def cabeçalho(txt):
    """
    Cabecalho para facilidar a reproducao dos menus e opcoes pincipais
    """
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for e, j in enumerate(lista):
        print(f'\033[1;33m{e+1}\033[m - \033[1;36m{j}\033[m')
    escolha = leiaInt('\033[1;33mDigite sua opção: \033[m')
    return escolha
    linha()
