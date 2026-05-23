# Este código demonstra o uso da biblioteca PyCUDA para realizar uma operação de adição de vetores na GPU. 
# Para executar este código, você precisa ter o PyCUDA instalado. 
# Você pode instalar o PyCUDA usando o comando: pip install pycuda
# Este exemplo cria dois vetores, os soma na GPU e imprime o resultado.

import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda import gpuarray

# Tamanho dos vetores
N = 10

# Criando dois vetores aleatórios
a = np.random.rand(N).astype(np.float32)
b = np.random.rand(N).astype(np.float32)

# Transferindo os vetores para a GPU
a_gpu = gpuarray.to_gpu(a)
b_gpu = gpuarray.to_gpu(b)

# Criando um vetor para armazenar o resultado
result_gpu = gpuarray.empty_like(a_gpu)

# Kernel CUDA para somar os vetores
mod = drv.SourceModule("""
__global__ void add(float *a, float *b, float *result)
{
    int idx = threadIdx.x;
    result[idx] = a[idx] + b[idx];
}
""")

# Obtendo a função do kernel
add_func = mod.get_function("add")

# Executando o kernel
add_func(a_gpu, b_gpu, result_gpu, block=(N, 1, 1))

# Transferindo o resultado de volta para a CPU
result = result_gpu.get()

# Imprimindo os resultados
print("Vetor A:", a)
print("Vetor B:", b)
print("Resultado da soma:", result)