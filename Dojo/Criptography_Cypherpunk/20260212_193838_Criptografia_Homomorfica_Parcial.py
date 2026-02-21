# Este código demonstra a criptografia homomórfica parcial usando a biblioteca PySEAL. 
# A criptografia homomórfica permite realizar operações em dados criptografados sem precisar descriptografá-los. 
# Para executar este código, instale a biblioteca PySEAL com: pip install pyseal.

from seal import EncryptionParameters, SEALContext, KeyGenerator, Encryptor, Decryptor, Evaluator, IntegerEncoder, Plaintext, Ciphertext

# Configuração dos parâmetros de criptografia
parms = EncryptionParameters()
parms.set_poly_modulus_degree(4096)
parms.set_coeff_modulus([1 << 40, 1 << 40, 1 << 40])
parms.set_plain_modulus(1 << 8)

context = SEALContext(parms)
keygen = KeyGenerator(context)
encryptor = Encryptor(context, keygen.secret_key())
decryptor = Decryptor(context, keygen.secret_key())
evaluator = Evaluator(context)
encoder = IntegerEncoder(context)

# Criptografando dois números
num1 = 5
num2 = 10
plain1 = encoder.encode(num1)
plain2 = encoder.encode(num2)

cipher1 = Ciphertext()
cipher2 = Ciphertext()
encryptor.encrypt(plain1, cipher1)
encryptor.encrypt(plain2, cipher2)

# Realizando a soma em dados criptografados
cipher_result = Ciphertext()
evaluator.add(cipher1, cipher2, cipher_result)

# Descriptografando o resultado
plain_result = Plaintext()
decryptor.decrypt(cipher_result, plain_result)
result = encoder.decode(plain_result)

print(f"O resultado da soma de {num1} e {num2} é: {result}")