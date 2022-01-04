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


def leiafloat(msg):
    while True:
        try:
            x = float(input('Digite um número real: '))
        except ValueError:
            print(f'\033[31mERRO! Por favor digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return x


n1 = leiaInt('Digite um número: ')
n2 = leiafloat('Digite um número: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')