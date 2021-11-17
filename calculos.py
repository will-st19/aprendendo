def verifica_numero(num):
    try:
        float(num)
        return True
    except:
        pass

    return False


def somar(num1, num2):
    return float(num1) + float(num2)


def subtrair(num1, num2):
    return float(num1) - float(num2)


def multiplicar(num1, num2):
    return float(num1) * float(num2)


def dividir(num1, num2):
    return float(num1) / float(num2)


while True:
    valor1 = input('Digite o primeiro valor: ')
    valor2 = input('Digite o segundo valor: ')

    print("/*" * 20)

    if verifica_numero(valor1) and verifica_numero(valor2):
        print(f'Resultado da soma = {somar(valor1, valor2):.0f}')
        print(f'Resultado da subtração = {subtrair(valor1, valor2):.0f}')
        print(f'Resultado da multiplicação = {multiplicar(valor1, valor2):.0f}')

        if valor2 != "0":
            print(f'Resultado da divisão = {dividir(valor1, valor2):.2f}')
        else:
            print('Não foi possível fazer a divisão!')
    else:
        print('Não foi possível fazer os cálculos')

    print("/*" * 20)

    continuar = str(input("\nContinuar? [S/N] ")).upper()
    if continuar == "N":
        break
    else:
        print()