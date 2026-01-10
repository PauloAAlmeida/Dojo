# Este código demonstra a redução paralela usando a biblioteca Numba para somar todos os elementos de um array em paralelo. 
# Para executar este código, você precisa instalar a biblioteca Numba com o comando: 
# pip install numba
# O código utiliza a função @njit para compilar a função de soma para execução em GPU.

import numpy as np
from numba import cuda

@cuda.jit
def soma_array(arr, resultado):
    idx = cuda.grid(1)
    if idx < arr.size:
        cuda.atomic.add(resultado, 0, arr[idx])

def soma_paralela(arr):
    resultado = np.zeros(1, dtype=np.float32)
    d_arr = cuda.to_device(arr)
    threads_per_block = 256
    blocks_per_grid = (arr.size + (threads_per_block - 1)) // threads_per_block
    soma_array[blocks_per_grid, threads_per_block](d_arr, resultado)
    return resultado[0]

# Exemplo de uso
array = np.random.rand(1000000).astype(np.float32)
soma_total = soma_paralela(array)
print(f"A soma total dos elementos do array é: {soma_total}")