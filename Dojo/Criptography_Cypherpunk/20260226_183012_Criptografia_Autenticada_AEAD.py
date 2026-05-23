# Este código demonstra a criptografia autenticada usando o modo GCM (Galois/Counter Mode) com a biblioteca `cryptography`. 
# Para executar este código, instale a biblioteca com: pip install cryptography
# O código irá gerar uma chave, criptografar uma mensagem e, em seguida, descriptografá-la, 
# garantindo a integridade e autenticidade dos dados.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Gerar chave e IV
key = os.urandom(32)  # 256 bits
iv = os.urandom(12)   # 96 bits

# Mensagem a ser criptografada
plaintext = b"Mensagem secreta"
aad = b"Dados adicionais"  # Dados que não precisam ser criptografados, mas que serão autenticados

# Criptografar
cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
encryptor = cipher.encryptor()
encryptor.authenticate_additional_data(aad)
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
tag = encryptor.tag

# Descriptografar
cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
decryptor = cipher.decryptor()
decryptor.authenticate_additional_data(aad)
decrypted_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Resultados
print("Texto original:", plaintext)
print("Texto criptografado:", ciphertext)
print("Texto descriptografado:", decrypted_plaintext)