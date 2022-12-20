class Calculadora:

        def soma(self, valor_a, valor_b):
            return valor_a + valor_b
        
        def subtracao (self, valor_a, valor_b):
            return valor_a - valor_b
        
        def multiplicacao(self, valor_a, valor_b):
            return valor_a * valor_b
        
        def divisao(self, valor_a, valor_b):
            return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(5,2))
print(calculadora.subtracao(7,4))
print(calculadora.multiplicacao(3,9))
print(calculadora.divisao(8,2))