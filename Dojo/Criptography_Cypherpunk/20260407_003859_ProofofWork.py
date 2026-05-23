# Este código implementa um conceito básico de Proof-of-Work utilizando Hashcash. 
# O objetivo é encontrar um nonce que, quando combinado com um dado, gera um hash 
# que começa com um número específico de zeros. Isso simula o trabalho computacional 
# necessário para validar transações em criptomoedas.

import hashlib
import time

def hashcash(difficulty, data):
    nonce = 0
    while True:
        input_data = f"{data}{nonce}".encode()
        hash_result = hashlib.sha256(input_data).hexdigest()
        if hash_result.startswith('0' * difficulty):
            return nonce, hash_result
        nonce += 1

if __name__ == "__main__":
    data = "Exemplo de Hashcash"
    difficulty = 4  # Número de zeros iniciais desejados
    start_time = time.time()
    nonce, hash_result = hashcash(difficulty, data)
    elapsed_time = time.time() - start_time
    print(f"Nonce encontrado: {nonce}")
    print(f"Hash resultante: {hash_result}")
    print(f"Tempo gasto: {elapsed_time:.2f} segundos")