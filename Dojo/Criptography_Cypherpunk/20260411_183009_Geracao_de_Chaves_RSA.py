# Este código gera um par de chaves RSA (pública e privada) usando a biblioteca `cryptography`. 
# Para executar este código, instale a biblioteca com o comando: 
# pip install cryptography
# O código gera duas chaves e imprime seus valores em formato PEM.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gera a chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Gera a chave pública
public_key = private_key.public_key()

# Serializa a chave privada
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL
)

# Serializa a chave pública
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Imprime as chaves
print("Chave Privada:\n", private_pem.decode('utf-8'))
print("Chave Pública:\n", public_pem.decode('utf-8'))