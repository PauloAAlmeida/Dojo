# Este código demonstra a diferença entre funções com complexidade O(n) e O(n²). 
# A função O(n) realiza uma soma simples de elementos em uma lista, 
# enquanto a função O(n²) compara todos os pares de elementos. 
# Vamos observar como o tempo de execução varia com o tamanho da entrada.

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
    start = time.time()
    funcao_O_n(tamanho)
    end = time.time()
    print(f"O(n) para n={tamanho}: {end - start:.6f} segundos")

    start = time.time()
    funcao_O_n2(tamanho)
    end = time.time()
    print(f"O(n²) para n={tamanho}: {end - start:.6f} segundos")