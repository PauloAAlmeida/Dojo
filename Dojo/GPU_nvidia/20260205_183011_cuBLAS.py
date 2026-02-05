# Este código demonstra a multiplicação de matrizes usando a biblioteca cuBLAS da NVIDIA, que é otimizada para execução em GPUs. Para rodar este código, é necessário ter o CUDA Toolkit instalado e a biblioteca cuBLAS disponível. Você pode instalar o CUDA Toolkit a partir do site da NVIDIA. O código cria duas matrizes aleatórias e utiliza cuBLAS para calcular o produto delas.

import numpy as np
import cupy as cp

# Definindo as dimensões das matrizes
N = 1024

# Criando matrizes aleatórias
A = cp.random.rand(N, N).astype(cp.float32)
B = cp.random.rand(N, N).astype(cp.float32)

# Inicializando a matriz resultado
C = cp.empty((N, N), dtype=cp.float32)

# Multiplicação de matrizes usando cuBLAS
cp.cuda.cublas.cublasSgemm(cp.cuda.cublas.cublasCreate(), 'n', 'n', N, N, N, 
                            1.0, A.data.ptr, N, B.data.ptr, N, 
                            0.0, C.data.ptr, N)

# Convertendo o resultado para numpy para impressão
C_np = cp.asnumpy(C)

# Imprimindo uma parte do resultado
print(C_np[:5, :5])  # Imprime os primeiros 5x5 elementos da matriz resultado