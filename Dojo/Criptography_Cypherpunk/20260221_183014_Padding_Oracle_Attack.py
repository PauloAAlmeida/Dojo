# Este código simula um ataque de Padding Oracle, onde um atacante tenta decifrar uma mensagem criptografada ao explorar erros de padding. 
# Ele simula um servidor que responde com um erro se o padding da mensagem decifrada estiver incorreto. 
# O atacante tenta descobrir a mensagem original testando bytes um por um. 
# Para rodar este código, não são necessárias bibliotecas externas.

def padding_oracle_attack(ciphertext):
    # Simula a resposta de um servidor com erro de padding
    def oracle(plaintext):
        try:
            # Simula a verificação de padding
            if plaintext[-1] == 1:
                raise ValueError("Invalid padding")
            return True
        except ValueError:
            return False

    block_size = 16
    plaintext = bytearray()
    
    for i in range(len(ciphertext) // block_size):
        block = ciphertext[i * block_size:(i + 1) * block_size]
        for padding_value in range(1, block_size + 1):
            for byte in range(256):
                # Cria um novo bloco com o byte testado
                modified_block = bytearray(block)
                modified_block[-padding_value] = byte
                modified_block[-padding_value + 1:] = bytes([padding_value] * (padding_value - 1))
                
                # Verifica se o padding é válido
                if oracle(modified_block):
                    plaintext.append(byte ^ padding_value)
                    break

    return plaintext

# Mensagem cifrada simulada (exemplo)
ciphertext = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10])
plaintext = padding_oracle_attack(ciphertext)
print("Mensagem decifrada:", plaintext)