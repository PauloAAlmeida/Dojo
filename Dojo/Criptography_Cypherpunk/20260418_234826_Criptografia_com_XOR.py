# Este código implementa uma cifra de fluxo básica usando a operação XOR para criptografar e descriptografar mensagens. 
# A cifra XOR é uma técnica simples de criptografia simétrica onde a mensagem é combinada com uma chave usando a operação lógica XOR. 
# Para rodar este código, não são necessárias bibliotecas externas. 

def xor_encrypt_decrypt(message, key):
    return ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))

# Exemplo de uso
mensagem = "Ola, Mundo!"
chave = "chave123456"  # A chave deve ter o mesmo comprimento da mensagem

# Criptografar
mensagem_criptografada = xor_encrypt_decrypt(mensagem, chave)
print("Mensagem Criptografada:", mensagem_criptografada)

# Descriptografar
mensagem_descriptografada = xor_encrypt_decrypt(mensagem_criptografada, chave)
print("Mensagem Descriptografada:", mensagem_descriptografada)