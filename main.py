import pytest

# Funções que fazem as contas

def somar_dois_numeros(num1, num2):
    return num1 + num2


def subtrair_dois_numeros(num1, num2):
    return num1 - num2


def multiplicar_dois_numeros(num1, num2):
    return num1 * num2


def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return ' Não é possível dividir o zero'


def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2


def calcular_area_do_quadrado(num1):
    return num1 ** num1


def calcular_area_de_um_retangulo(base, altura):
    return base * altura


def calcular_area_de_um_triangulo(base, altura, num3):
    return (base * altura) / num3

#Area = Pi * raio **2
def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2






#Chamam as funções

if __name__ == '__main__':
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')

    resultado = subtrair_dois_numeros(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(7, 5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(7, 0)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_do_quadrado(2)
    print(f'A área do quadro é {resultado}')

    resultado = calcular_area_de_um_retangulo(2, 3)
    print(f' A área do retângulo é {resultado}')

    resultado = calcular_area_de_um_triangulo(3, 2, 2)
    print(f' A área do triângulo é {resultado}')



