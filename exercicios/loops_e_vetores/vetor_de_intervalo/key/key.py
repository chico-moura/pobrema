def criar_vetor_a_partir_de_intervalo(inicio: int, fim: int) -> [int]:
    if inicio < fim:
        actual_range = range(inicio, fim + 1)
    else:
        actual_range = reversed(range(fim, inicio + 1))
    return [n for n in actual_range]
