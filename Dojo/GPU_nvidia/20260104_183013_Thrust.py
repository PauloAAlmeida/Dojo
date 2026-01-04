# Este código demonstra o uso da biblioteca Thrust para realizar operações paralelas em vetores. 
# O Thrust é uma biblioteca de C++ que facilita a programação paralela em GPUs. 
# Para usar este exemplo, você precisará do CUDA Toolkit instalado em sua máquina. 
# Este snippet não é executável diretamente em Python, mas é uma representação do que seria feito em C++.
# Para executar, você deve compilar com um compilador que suporte CUDA.

import numpy as np
from numba import cuda

@cuda.jit
def add_arrays(a, b, c):
    idx = cuda.grid(1)
    if idx < c.size:
        c[idx] = a[idx] + b[idx]

# Tamanho do vetor
n = 1000000
a = np.random.rand(n).astype(np.float32)
b = np.random.rand(n).astype(np.float32)
c = np.empty_like(a)

# Definindo o número de threads e blocos
threads_per_block = 256
blocks_per_grid = (n + (threads_per_block - 1)) // threads_per_block

# Executando o kernel
add_arrays[blocks_per_grid, threads_per_block](a, b, c)

# Imprimindo os primeiros 10 resultados
print(c[:10])