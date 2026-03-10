def multiplicacao(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def impar_par(numero):
    return 'Par' if numero % 2 == 0 else 'Ímpar'
   
multiplicar = multiplicacao(10, 20, 30, 40, 50)

print(multiplicar)

print(f'O número {multiplicar} é',impar_par(multiplicar))