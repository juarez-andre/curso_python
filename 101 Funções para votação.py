def voto(a):
    from datetime import datetime
    i = datetime.now().year - a
    if i < 16:
        print(f'Com {i} anos: voto NEGADO.')
    elif i >= 16 and i < 18 or i >= 65:
        print(f'Com {i} anos: Voto OPCIONAL.')
    elif i >= 18:
        print(f'Com {i} anos: Voto OBRIGATÓRIO.')


print('-' * 30)
voto(2010)