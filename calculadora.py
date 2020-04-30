class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def dividir(self):
        return self.a / self.b

    def multiplicar(self):
        return self.a * self.b

    def subtrair(self):
        return self.a - self.b


class Pessoa:

    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def imprimir(self):
        return '["id": "{}", "nome": "{}", "telefone": "{}"]'.format(self.id, self.nome, self.telefone)


