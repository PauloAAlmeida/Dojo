# Este código implementa um bloco simples de uma blockchain mínima, onde cada bloco contém um hash do bloco anterior. 
# A ideia é demonstrar como os blocos estão interligados, garantindo a integridade dos dados. 
# Para simplificar, utilizamos a biblioteca hashlib para gerar o hash. 
# Certifique-se de que a biblioteca hashlib está disponível (padrão em Python).

import hashlib
import json
from time import time

class Bloco:
    def __init__(self, index, timestamp, dados, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.hash = self.gerar_hash()

    def gerar_hash(self):
        bloco_str = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(bloco_str).hexdigest()

# Criando o bloco gênesis
bloco_genesis = Bloco(0, time(), "Bloco Gênesis", "0")
print(f'Bloco Gênesis: {bloco_genesis.__dict__}')

# Criando um segundo bloco
bloco_1 = Bloco(1, time(), "Segundo Bloco", bloco_genesis.hash)
print(f'Segundo Bloco: {bloco_1.__dict__}')