def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('-' * 40)
        print(f'{"PESSOAS CADASTRADAS":^40}')
        print('-' * 40)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecudi', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()



def leiaInt(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return x
