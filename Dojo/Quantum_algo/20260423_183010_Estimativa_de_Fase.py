# Este código utiliza a biblioteca Qiskit para estimar a fase de um operador unitário, que é um problema fundamental em computação quântica. 
# A estimativa de fase permite encontrar autovalores de operadores unitários, sendo essencial para algoritmos quânticos como o algoritmo de Shor. 
# Para executar este código, instale a biblioteca Qiskit com o comando: pip install qiskit.

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
import numpy as np

# Definindo o operador unitário U
theta = np.pi / 4  # Fase a ser estimada
U = QuantumCircuit(1)
U.rz(theta, 0)  # Aplicando a rotação em torno do eixo Z

# Criando o circuito de estimativa de fase
qc = QuantumCircuit(2, 1)
qc.h(0)  # Colocando o qubit de controle em superposição
qc.append(U.to_gate(), [0])  # Aplicando o operador unitário
qc.h(0)  # Aplicando a Hadamard novamente
qc.measure(0, 0)  # Medindo o qubit de controle

# Executando o circuito
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts()

# Imprimindo os resultados
print("Resultados da medição:", counts)