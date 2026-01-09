# Este código demonstra a insegurança do modo de operação ECB (Electronic Codebook) em comparação com CBC (Cipher Block Chaining) usando imagens. O ECB não embaralha os blocos de dados, resultando em padrões visíveis, enquanto o CBC oferece maior segurança ao misturar os blocos. Para executar o código, instale as bibliotecas necessárias com: pip install pillow pycryptodome.

from PIL import Image
from Crypto.Cipher import AES
import numpy as np

def encrypt_ecb(plain_image, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_image = cipher.encrypt(plain_image)
    return encrypted_image

def encrypt_cbc(plain_image, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = b'1234567890123456'  # IV deve ser aleatório em produção
    encrypted_image = cipher.encrypt(plain_image)
    return encrypted_image

def main():
    # Carregar uma imagem e converter para bytes
    img = Image.open('imagem.png').convert('RGB')
    img_data = np.array(img).flatten()
    img_data = img_data.tobytes()
    
    # Ajustar o tamanho da imagem para múltiplos de 16 bytes
    while len(img_data) % 16 != 0:
        img_data += b'\x00'
    
    key = b'1234567890123456'  # Chave de 16 bytes
    encrypted_ecb = encrypt_ecb(img_data, key)
    encrypted_cbc = encrypt_cbc(img_data, key)
    
    # Salvar as imagens criptografadas (apenas para visualização)
    ecb_image = Image.frombytes('RGB', img.size, encrypted_ecb)
    cbc_image = Image.frombytes('RGB', img.size, encrypted_cbc)
    
    ecb_image.save('ecb_encrypted.png')
    cbc_image.save('cbc_encrypted.png')

main()