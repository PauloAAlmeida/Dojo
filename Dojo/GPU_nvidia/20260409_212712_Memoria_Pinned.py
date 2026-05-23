# Este código compara a transferência de dados entre a memória paginada e a memória pinned usando a biblioteca CuPy, que é uma interface semelhante ao NumPy, mas que utiliza a GPU. Para executar este código, instale a biblioteca CuPy com o comando: `pip install cupy`. O código mede o tempo necessário para transferir dados de um array grande para a GPU usando ambos os métodos.

import cupy as cp
import numpy as np
import time

# Tamanho do array
N = 10**7

# Criando um array grande na memória paginada (CPU)
data = np.random.rand(N)

# Transferência usando memória paginada
start_time = time.time()
data_gpu_paged = cp.asarray(data)
end_time = time.time()
print(f"Tempo de transferência (memória paginada): {end_time - start_time:.6f} segundos")

# Transferência usando memória pinned
data_pinned = cp.asarray(data, order='C')
start_time = time.time()
data_gpu_pinned = cp.asarray(data_pinned)
end_time = time.time()
print(f"Tempo de transferência (memória pinned): {end_time - start_time:.6f} segundos")