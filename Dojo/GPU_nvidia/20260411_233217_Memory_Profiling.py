# Este código demonstra o uso de memória em uma operação simples de multiplicação de matrizes utilizando NumPy. 
# O objetivo é mostrar como o uso de GPU pode acelerar operações computacionais. 
# Para executar este código, é necessário ter o NumPy instalado. 
# Instale com: pip install numpy
# Execute com nvprof para análise de memória.

import numpy as np

# Definindo o tamanho das matrizes
N = 1000

# Criando duas matrizes aleatórias
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)

# Multiplicando as matrizes
C = np.dot(A, B)

# Imprimindo uma parte do resultado
print(C[:5, :5])  # Imprime os primeiros 5 elementos da matriz resultado