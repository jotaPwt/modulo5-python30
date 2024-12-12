def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calculadora():
    print('CALCULADORA')
    n1 = int(input('Digite um numero>'))
    n2 = int(input('Digite um numero>'))
    op = input('+  -  *  /')
    if op == '+':
        resultado = soma(n1, n2)
        print(resultado)
        