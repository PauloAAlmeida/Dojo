# Este código implementa um sistema simples de timestamping distribuído usando hashes. 
# Ele simula a criação de um bloco de timestamps que garantem a ordem cronológica dos eventos 
# de forma descentralizada. Para rodar o código, não são necessárias bibliotecas externas.
# O código utiliza a biblioteca hashlib para gerar hashes.

import hashlib
import time

class TimestampBlock:
    def __init__(self, previous_hash):
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(str(self.timestamp).encode() + str(self.previous_hash).encode()).hexdigest()

def create_chain(num_blocks):
    chain = []
    previous_hash = "0"  # Hash inicial
    for _ in range(num_blocks):
        block = TimestampBlock(previous_hash)
        chain.append(block)
        previous_hash = block.hash
    return chain

# Criando uma cadeia de 5 blocos de timestamps
blockchain = create_chain(5)

# Imprimindo os detalhes de cada bloco
for index, block in enumerate(blockchain):
    print(f"Bloco {index}:")
    print(f"Timestamp: {block.timestamp}")
    print(f"Hash anterior: {block.previous_hash}")
    print(f"Hash do bloco: {block.hash}\n")