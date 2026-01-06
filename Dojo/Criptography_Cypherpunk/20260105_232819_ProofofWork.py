# Este código implementa o conceito de Proof-of-Work utilizando o algoritmo Hashcash. 
# O objetivo é encontrar um nonce que, quando combinado com um cabeçalho de dados, 
# produz um hash que começa com um número específico de zeros. 
# Para rodar este código, certifique-se de ter o Python instalado.
# Não são necessárias bibliotecas externas.

import hashlib
import time

def hashcash(header, nonce):
    return hashlib.sha256(f"{header}{nonce}".encode()).hexdigest()

def proof_of_work(header, difficulty):
    nonce = 0
    prefix_str = '0' * difficulty
    while True:
        hash_result = hashcash(header, nonce)
        if hash_result.startswith(prefix_str):
            return nonce, hash_result
        nonce += 1

if __name__ == "__main__":
    header = "Exemplo de Hashcash"
    difficulty = 4  # Número de zeros iniciais desejados
    start_time = time.time()
    nonce, result_hash = proof_of_work(header, difficulty)
    end_time = time.time()
    
    print(f"Nonce encontrado: {nonce}")
    print(f"Hash resultante: {result_hash}")
    print(f"Tempo de execução: {end_time - start_time:.2f} segundos")