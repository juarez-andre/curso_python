p = int(input('Primeiro Valor: '))
s = int(input('Segundo Valor: '))
t = int(input('Terceiro Valor: '))
if p < s and p < t:
    print('O menor valor digitado foi {}.'.format(p))
if s < p and s < t:
    print('O menor valor digitado foi {}.'.format(s))
if t < p and t < s:
    print('O menor valor digitado foi {}.'.format(t))
if p == s and p < t:
    a = p
    print('O menor valor digitado foi {}(2x).'.format(a))
if s == t and s < p:
    a = s
    print('O menor valor digitado foi {}(2x).'.format(a))
if t == p and t < s:
    a = t
    print('O menor valor digitado foi {}(2x).'.format(a))
if t == p and t > s:
    a = t
    print('O maior valor digitado foi {}(2x).'.format(a))
if s == t and s > p:
    a = s
    print('O maior valor digitado foi {}(2x).'.format(a))
if p == s and p > t:
    a = p
    print('O maior valor digitado foi {}(2x).'.format(a))
if p > s and p > t:
    print('O maior valor digitado foi {}.'.format(p))
if s > p and s > t:
    print('O maior valor digitado foi {}.'.format(s))
if t > p and t > s:
    print('O maior valor digitado foi {}.'.format(t))
if p == s and s == t:
    print('O menor valor digitado foi {}(3x).'.format(p))
    print('O maior valor digitado foi {}(3x).'.format(p))
