from arquivo import *
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    try:
        print('-' * 40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('-' * 40)
        print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m ')
        print('\033[33m2 -\033[m \033[34mCadastrar nova Pessoa\033[m')
        print('\033[33m3 -\033[m \033[34mSair do Sistema\033[m')
        print('-' * 40)
        op = int(input('\033[33mSua opção: \033[m'))
    except (ValueError, TypeError):
        print('\033[31m ERRO! Digite uma opção válida!\033[m')
    else:
        if op > 3 or op < 0:
            print('\033[31m ERRO! Digite uma opção válida!\033[m')
        else:
            break
while True:
    while op == 1:
        lerArquivo(arq)
        op = int(input('\033[33mSua opção:\033[m'))
    while op == 2:
        nome = str(input('Nome:'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        op = int(input('\033[33mSua opção: \033[m '))
    if op == 3:
        print('-' * 40)
        print(f'{">> PROGRAMA ENCERRADO <<":^40}')
        print('-' * 40)
        break