from calculadora import Calculadora, Pessoa

def imprimir():
    print("Valor A: {}".format(calculo.a))
    print("Valor B: {}".format(calculo.b))
    print("+ = {}".format(calculo.soma()))
    print("- = {}".format(calculo.subtrair()))
    print("* = {}".format(calculo.multiplicar()))
    print("/  = {}".format(calculo.dividir()))

#instanciar uma classe em python:
calculo = Calculadora(1,2)

#imprimir dados
imprimir()

#*******************************************************

#incluir dados
pessoa = Pessoa(1,"andre", "16 8888-4454")

#imprimir
print(pessoa.imprimir())







