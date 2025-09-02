# calculadora_test.py

# --- FUNÇÕES DA CALCULADORA ---
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b


# --- TESTES ---
def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-1, -1) == -2

def test_somar_zero():
    assert somar(0, 5) == 5

def test_subtrair_positivos():
    assert subtrair(5, 3) == 2

def test_subtrair_negativos():
    assert subtrair(-1, -1) == 0

def test_subtrair_zero():
    assert subtrair(0, 5) == -5

def test_multiplicar_positivos():
    assert multiplicar(2, 3) == 6

def test_multiplicar_negativos():
    assert multiplicar(-1, -1) == 1

def test_multiplicar_zero():
    assert multiplicar(0, 5) == 0

def test_dividir_positivos():
    assert dividir(6, 3) == 2

def test_dividir_negativos():
    assert dividir(-4, -2) == 2

def test_dividir_zero():
    assert dividir(5, 0) == "Não é possível dividir por zero"

