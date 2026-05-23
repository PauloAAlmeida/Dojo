# Este código demonstra como calcular o hash SHA-256 de uma string em Python. 
# O SHA-256 é um algoritmo de hash criptográfico que gera um valor fixo de 256 bits. 
# Para executar este código, você precisa da biblioteca hashlib, que já vem com a instalação padrão do Python.
# O código também pode ser adaptado para calcular o hash de um arquivo.
# Vamos gerar o hash de uma string de exemplo.

import hashlib

# Função para gerar o hash SHA-256 de uma string
def calcular_hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

# String de exemplo
texto_exemplo = "Olá, mundo!"
hash_resultado = calcular_hash_sha256(texto_exemplo)

print(f"Texto: {texto_exemplo}")
print(f"Hash SHA-256: {hash_resultado}")