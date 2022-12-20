lista = [12,30,5,7]
lista_animal = ['cachorro', 'gato','elefante', 'lobo', 'arara']
print(lista_animal[1])
for x in lista_animal:
    print(x)
soma = 0
for x in lista:
    print(x)
    soma += x
nova_lista = lista_animal * 3
print(nova_lista)
if 'gato' in lista_animal:
    print('exite um gato na lista')
else: 
    print('tem não')
print(soma)
#soma simplificada
print(sum(lista))
print(max(lista))
print(min(lista))
print(min(lista_animal))
print(max(lista_animal))
if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else: 
    print('não tem um lobo na lista')
    lista_animal.append('lobo')
    print(lista_animal)
lista_animal.pop()
print(lista_animal)
lista_animal.remove('elefante')
print(lista_animal)
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

tupla = (1,10,12,14)
print(tupla)
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)