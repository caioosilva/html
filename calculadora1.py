class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    
    def menos(self):
        return self.a - self.b
    
    def vezes(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

calculadora = Calculadora(10, 2)
print(calculadora.a)
print(calculadora.soma())
print(calculadora.menos())
print(calculadora.vezes())
print(calculadora.div())