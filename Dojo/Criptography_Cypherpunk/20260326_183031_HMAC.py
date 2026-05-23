# Este código demonstra como gerar um código de autenticação de mensagem (HMAC) usando uma chave secreta. 
# O HMAC é uma função hash criptográfica que combina uma chave secreta com a mensagem original, 
# garantindo a integridade e autenticidade dos dados. 
# Para executar este código, você precisa da biblioteca `hmac`, que é padrão em Python, 
# e da biblioteca `hashlib`, também padrão em Python.

import hmac
import hashlib

# Chave secreta e mensagem
chave_secreta = b'minha_chave_secreta'
mensagem = b'minha_mensagem_importante'

# Gerar HMAC
hmac_resultado = hmac.new(chave_secreta, mensagem, hashlib.sha256).hexdigest()

# Imprimir o resultado
print("HMAC:", hmac_resultado)