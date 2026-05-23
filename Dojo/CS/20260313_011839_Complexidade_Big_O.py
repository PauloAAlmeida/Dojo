# Este código demonstra a diferença entre duas funções com complexidade de tempo O(n²) e O(n). 
# A função O(n²) realiza uma operação quadrática, enquanto a função O(n) realiza uma operação linear. 
# Ambas as funções recebem uma lista de números e executam operações diferentes. 
# O objetivo é mostrar como a complexidade afeta o tempo de execução conforme o tamanho da entrada.

import time

def funcao_O_n(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma

def funcao_O_n2(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += i + j
    return soma

tamanhos = [10, 100, 200]

for tamanho in tamanhos:
    inicio = time.time()
    funcao_O_n(tamanho)
    fim = time.time()
    print(f"O(n) para n={tamanho}: {fim - inicio:.6f} segundos")

    inicio = time.time()
    funcao_O_n2(tamanho)
    fim = time.time()
    print(f"O(n²) para n={tamanho}: {fim - inicio:.6f} segundos")