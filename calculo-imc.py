peso = float(input('peso: '))
altura = float(input('altura: '))

def imc():
    calc = peso//altura**2
    print(calc)

imc = imc()
print(imc)