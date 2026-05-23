# Este código demonstra a aplicação da porta Hadamard em computação quântica. 
# A porta Hadamard cria uma superposição de estados a partir do estado |0>. 
# Usaremos a biblioteca Qiskit para simular o circuito quântico. 
# Para instalar, execute: pip install qiskit

from qiskit import QuantumCircuit, Aer, execute

# Criar um circuito quântico com 1 qubit
circuit = QuantumCircuit(1)

# Aplicar a porta Hadamard ao qubit
circuit.h(0)

# Medir o qubit
circuit.measure_all()

# Simular o circuito
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1024).result()

# Obter e imprimir os resultados
counts = result.get_counts(circuit)
print(counts)