from interface import cabeçalho


def arquivo_yes(nome):
    """
    -> Funcao para verificar se já existe um arquiv txt gerado
    recebe como parametro o nome do arquivo
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arq(nome):
    """
    -> Em caso de não haver arquivo gerado, é criado um novo arquivo
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome}, criado com sucesso!')


def ler_arquivo(nome):
    """
    -> funcao para ler e mostra o arquivo txt, que matem os dados de usuarios cadastrados
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    """"
    -> função para cadastrar um novo usuario no arquivo txt
    """
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao incluir novo cadastro')
        else:
            print('Novo registro salvo com sucesso')
            a.close()

