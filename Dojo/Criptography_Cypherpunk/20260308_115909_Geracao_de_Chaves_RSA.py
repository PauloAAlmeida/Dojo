# Este código gera um par de chaves RSA (pública e privada) utilizando a biblioteca `cryptography`. 
# Para executar este código, instale a biblioteca com o comando: 
# pip install cryptography
# O código gera as chaves e as imprime no formato PEM.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gera um par de chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

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
print("Chave Privada:")
print(private_pem.decode('utf-8'))
print("Chave Pública:")
print(public_pem.decode('utf-8'))