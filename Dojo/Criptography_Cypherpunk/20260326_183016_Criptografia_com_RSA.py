# Este código demonstra a criptografia RSA, onde uma mensagem é criptografada usando uma chave pública e, em seguida, descriptografada com a chave privada. Para executar este código, você precisará instalar a biblioteca `cryptography` usando o comando `pip install cryptography`.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Geração de chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Mensagem original
message = b"Mensagem secreta"
print(f"Mensagem original: {message.decode()}")

# Criptografar com chave pública
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Mensagem criptografada: {ciphertext}")

# Descriptografar com chave privada
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Mensagem descriptografada: {decrypted_message.decode()}")