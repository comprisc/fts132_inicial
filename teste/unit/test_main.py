import pytest

from main import somar_dois_numeros, calcular_area_de_um_triangulo, calcular_area_de_um_retangulo, \
    calcular_area_do_quadrado, elevar_um_numero_pelo_outro, calcular_area_do_circulo


def testar_somar_dois_numero():

    num1 = 8
    num2 = 9

    resultado_esperado = 17

    resultado_atual = somar_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado


def testar_elevar_um_numero_pelo_outro():
    num1 = 2
    num2 = 3
    resultado_esperado = 8

    assert resultado_esperado == elevar_um_numero_pelo_outro(num1, num2)


def testar_calcular_area_do_quadrado():
    num1 = 2
    resultado_esperado = 4

    assert resultado_esperado == calcular_area_do_quadrado(num1)


def testar_calcular_area_do_retangulo():
    base = 2
    altura = 3

    resultado_esperado = 6

    assert resultado_esperado == calcular_area_de_um_retangulo(base, altura)


def testar_calcular_area_de_um_triangulo():
    base = 3
    altura = 2
    num3 = 2

    resultado_esperado = 3

    assert resultado_esperado == calcular_area_de_um_triangulo(base, altura, num3)

def testar_calculo_do_circulo():
    # Configura
    raio = 1
    resultado_esperado = 3.14

    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Validar
    assert resultado_atual == resultado_esperado

