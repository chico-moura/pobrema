def criar_vetor_crescente(tamanho: int) -> [int]:
    return [num for num in range(tamanho)]


def criar_vetor_decrescente(tamanho: int) -> [int]:
    return [num for num in reversed(range(tamanho))]


def criar_vetor_de_intervalo(inicio: int, fim: int) -> [int]:
    if inicio < fim:
        actual_range = range(inicio, fim + 1)
    else:
        actual_range = reversed(range(fim, inicio + 1))
    return [num for num in actual_range]
