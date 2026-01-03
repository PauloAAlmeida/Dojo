# Este código simula a notarização de documentos ao ancorar o hash de um documento em uma blockchain simulada. 
# A blockchain é representada por uma lista de blocos, onde cada bloco contém um hash do documento e o hash do bloco anterior. 
# Isso garante a integridade e a imutabilidade dos registros. 
# Para executar, não são necessárias bibliotecas externas.

import hashlib
import time

class Bloco:
    def __init__(self, indice, hash_documento, hash_anterior):
        self.indice = indice
        self.hash_documento = hash_documento
        self.hash_anterior = hash_anterior
        self.timestamp = time.time()
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        valor = f"{self.indice}{self.hash_documento}{self.hash_anterior}{self.timestamp}"
        return hashlib.sha256(valor.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadeia = []
        self.criar_bloco(genesis=True)

    def criar_bloco(self, hash_documento=None):
        indice = len(self.cadeia) + 1
        hash_anterior = self.cadeia[-1].hash if self.cadeia else "0"
        novo_bloco = Bloco(indice, hash_documento, hash_anterior)
        self.cadeia.append(novo_bloco)
        return novo_bloco

    def notarizar_documento(self, documento):
        hash_documento = hashlib.sha256(documento.encode()).hexdigest()
        bloco = self.criar_bloco(hash_documento)
        return bloco.hash

# Exemplo de uso
blockchain = Blockchain()
documento = "Este é um documento importante."
hash_notarizado = blockchain.notarizar_documento(documento)
print(f"Hash do documento notarizado: {hash_notarizado}")
print(f"Número de blocos na blockchain: {len(blockchain.cadeia)}")