# calculadora.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("Calculadora Simples")
print(" 2 - 3 =", subtrair(2, 3))
print(" 2 / 0 =", dividir(2, 0))