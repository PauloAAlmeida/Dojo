# Este código utiliza a biblioteca Qiskit para realizar a tomografia de estado quântico. 
# A tomografia de estado é um processo que permite reconstruir o estado quântico de um sistema a partir de medições realizadas. 
# Para executar este código, instale o Qiskit com o comando: 
# pip install qiskit
# O código cria um estado quântico, realiza medições e reconstrói o estado.

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector
import numpy as np

# Criar um circuito quântico com 1 qubit
qc = QuantumCircuit(1)
qc.h(0)  # Aplica uma porta Hadamard
qc.measure_all()

# Simular o circuito
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts()

# Calcular a probabilidade de cada estado
probabilities = {key: value / 1024 for key, value in counts.items()}
print("Resultados das medições:", probabilities)

# Reconstruir o vetor de estado
theta = 2 * np.arccos(np.sqrt(probabilities.get('0', 0)))
phi = 0  # Para simplificação, consideramos phi = 0
state_vector = [np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)]
print("Vetor de estado reconstruído:", state_vector)

# Visualizar o vetor de estado no plano de Bloch
plot_bloch_multivector(state_vector).show()