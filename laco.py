for x in range(101):
    print(x)
# numero primo a partir da entrada
a = int(input('entre com um número: '))
div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1
if div ==2:
    print('número {} é primo'.format(a))
else:
    print('número {} nâo é primo'.format(a))
#numeros primos a partir do laço
for i in range(101):
    div = 0
    for x in range (1, i+1):
        resto = i % x
        print(x,resto)
        if resto == 0:
            div += 1
    if div == 2:
       print(i)
#até o numero que for colocado pelo usuario
a = int(input('Digita um numero ae parsa: '))
for i in range(a+1):
    div = 0
    for x in range (1, i+1):
        resto = i % x
        print(x,resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(i)

# while/contar
a = 0
while a <= 10:
    print(a)
    a += 1

# min e max com while
nota1 = int(input('digite a nota do primeiro bi: '))
while nota1 > 10:
    nota1 = int(input('ta dificil ai parsa??? arruma essa bagaça so 0-10: '))
nota2 = int(input('digite a nota do segundo bi: '))
while nota2 > 10:
    nota2 = int(input('ta dificil ai parsa??? arruma essa bagaça so 0-10: '))
nota3 = int(input('digite a nota do terceiro bi: '))
while nota3 > 10:
    nota3 = int(input('ta dificil ai parsa??? arruma essa bagaça so 0-10: '))
nota4 = int(input('digite a nota do quarto bi: '))
while nota3 > 10:
    nota3 = int(input('ta dificil ai parsa??? arruma essa bagaça so 0-10: '))