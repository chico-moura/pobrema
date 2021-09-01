"""

Escreva as duas funções:
    selecionar_pares()
    selecionar_impares()
    
Cada uma delas rececbe como argumento um vetor de inteiros.
Cada uma deve retornar um vetor de inteiros.

Tente não se repetir.

"""
from src.solution.loops_e_vetores import ParImpar


def selecionar_pares(numeros: [int]) -> [int]:
    #return [num for num in numeros if num % 2 == 0]
    pass


def selecionar_impares(numeros: [int]) -> [int]:
    #return [num for num in numeros if num % 2 == 2]
    pass

# Pode declarar funções auxiliares abaixo, mas não mude o nome das funções acima


# Não mexa pessa parte :)
ParImpar(selecionar_pares, selecionar_impares).solve()
