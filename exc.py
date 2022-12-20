lista = [1,10]
arquivo = open('velho.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10/0
    numero = lista[1]
    print('fechando arquivo')
    arquivo.close()
except ArithmeticError:
    print('houve um erro ao realizar uma operacao aritmaetivca')
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')
except IndexError:
    print('não existe na lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('executa quando nao ocorrer exceção')
finally:
    print('sempre executa')
    arquivo.close()