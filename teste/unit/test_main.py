import pytest

from main import somar_dois_numeros, calcular_area_de_um_triangulo, calcular_area_de_um_retangulo, \
    calcular_area_do_quadrado, elevar_um_numero_pelo_outro, calcular_area_do_circulo


def testar_somar_dois_numero():
    num1 = 8
    num2 = 9

    resultado_esperado = 17

    resultado_atual = somar_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado


# anotação para utilizar como massa de teste

@pytest.mark.parametrize('raio, resultado_esperado',
                         [(1, 3.14),  # teste nº 1
                          (2, 12.56),  # teste nº 2
                          (3, 28.26),  # teste nº 3
                          (4, 50.24),  # teste nº 4
                          ('a','Falha no calculo. Raio não é um número'),  # teste nº5
                          (' ', 'Falha no calculo. Raio não é um número')
                        ])
def testar_calculo_do_circulo(raio, resultado_esperado):
    # Configura / Comentamos para que os parametros sejam lidos
    # raio = 1
    # resultado_esperado = 3.14

    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Validar
    assert resultado_atual == resultado_esperado
#oi 12