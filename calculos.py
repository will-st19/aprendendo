def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def dividir(num1, num2):
    return num1 / num2


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))


print(f'Resultado da soma = {somar(valor1, valor2)}')
print(f'Resultado da subtração = {subtrair(valor1, valor2)}')

if valor2 != 0:
    print(f'Resultado da divisão = {dividir(valor1, valor2):.2f}')
else:
    print('Não foi possível fazer a divisão!')