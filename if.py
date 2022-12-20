a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('tercerio valor: '))
if a > b and a > c:
    print('o maior número é: {}'.format(a))
elif b > a and b > c:
    print('O maior nuémro é: {}'.format(b))
else:
    print('o maior número é: {}'.format(c))
print('acabou viado')
a = int(input('Coloque um valor: '))
b = int(input('coloque outro valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or  not resto_b > 0:
    print('foi digitado número par')
else: 
    print('nao foi digitado par')
a = int(input('primeiro bi: '))
if a > 10:
    a = int(input('Cagou viado arruma essa merda, PRIMEIRO BIMESTRE JUMENTO: '))
b = int(input('segundo bi: '))
if b > 10:
    b = int(input('Errouuuuuuuuu. Segundo Bimestre: '))
c = int(input('terceiro bi: '))
if c > 10:
    c = int(input('Boa Champs, aposenta. Terceiro Bimestre: '))
d = int(input('quarto bi: '))
if d > 10:
    d = int(input('só não é mais bosta pq nasceu de uma buceta. Quarto Bimestre: '))
media = (a+b+c+d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('cagaram aqui')