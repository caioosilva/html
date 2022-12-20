conjunto = {1,2,3,4}
conjunto.add(5)
conjunto.discard(2)
print(type(conjunto))
print(conjunto)
conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8,9}
conjunto_uniao = conjunto.union(conjunto2)
print('uniao: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('interseccao: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferenca1: {}'.format(conjunto_diferenca1))
print('diferenca2: {}'.format(conjunto_diferenca2))
conjunto_difsim = conjunto.symmetric_difference(conjunto2)
print('diferenca simetrica: {}'.format(conjunto_difsim))
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('a é subconjunto de b?: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('b é um superconjunto de a?: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)