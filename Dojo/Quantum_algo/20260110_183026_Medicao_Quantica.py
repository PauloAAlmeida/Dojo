# Este código simula o colapso de uma função de onda em um sistema quântico simples. 
# Utiliza a biblioteca NumPy para manipulação de vetores e probabilidades. 
# Para instalar a biblioteca, execute: pip install numpy
import numpy as np

# Definindo a função de onda como um vetor de estados
def funcao_de_onda():
    estados = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # Superposição de |0> e |1>
    probabilidades = np.abs(estados)**2  # Calculando as probabilidades
    resultado = np.random.choice([0, 1], p=probabilidades)  # Colapso da função de onda
    return resultado

# Simulando a medição quântica
medicao = funcao_de_onda()
print(f'O resultado da medição quântica é: {medicao}')