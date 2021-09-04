"""

Escreva funções que retornam vetores de inteiros


criar_vetor_creescente():

Deve retornar um vetor onde cada espaço é ocupado pelo inteiro que também representa seu índice.
Recebe como argumento um inteiro e o chama de 'tamanho'.
Começando de 0, o vetor deve conter 'tamanho' espaços.

Exemplo:
    criar_vetor_crescente(5)

    ==

    [0, 1, 2, 3, 4]



criar_vetor_creescente():

Identica à criar_vetor_crescente(), mas a contagem é ao contrário: começa de 'tamanho' e termina em 0.

Exemplo:
    criar_vetor_decrescente(5)

    ==

    [4, 3, 2, 1, 0]

"""

from key import VetoresOrdenados


def criar_vetor_crescente(tamanho: int) -> [int]:
    # Escreva aqui
    pass


def criar_vetor_decrescente(tamanho: int) -> [int]:
    # Escreva aqui
    pass


# Não altere a linha abaixo
VetoresOrdenados(criar_vetor_crescente, criar_vetor_decrescente).solve()
