# Este código calcula a ocupação de um Multiprocessador Streaming (SM) em uma GPU NVIDIA. 
# A ocupação é a relação entre o número de threads ativas e o número máximo de threads que o SM pode suportar. 
# Isso é importante para otimizar o desempenho de kernels em CUDA. 
# Para executar este código, você precisa do pacote NumPy: `pip install numpy`.

import numpy as np

def calcular_ocupacao(num_threads_por_bloco, num_blocos, max_threads_por_SM):
    total_threads = num_blocos * num_threads_por_bloco
    ocupacao = (total_threads / max_threads_por_SM) * 100
    return ocupacao

# Parâmetros de exemplo
num_threads_por_bloco = 256  # Threads por bloco
num_blocos = 16               # Número de blocos
max_threads_por_SM = 1024     # Máximo de threads por SM

ocupacao = calcular_ocupacao(num_threads_por_bloco, num_blocos, max_threads_por_SM)
print(f"A ocupação do SM é: {ocupacao:.2f}%")