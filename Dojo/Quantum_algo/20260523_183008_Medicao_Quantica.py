# Este código simula o colapso da função de onda em um sistema quântico simples. 
# Ele utiliza a biblioteca NumPy para gerar um vetor de estado e realizar a medição. 
# Para instalar a biblioteca, execute: pip install numpy
import numpy as np

# Definindo um vetor de estado quântico (superposição)
estado = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # |0> e |1> com igual probabilidade

# Realizando a medição
resultado = np.random.choice([0, 1], p=[0.5, 0.5])

# Colapso da função de onda
if resultado == 0:
    estado_colapsado = np.array([1, 0])  # Colapsa para |0>
else:
    estado_colapsado = np.array([0, 1])  # Colapsa para |1>

print(f"Resultado da medição: {resultado}")
print(f"Estado colapsado: {estado_colapsado}")