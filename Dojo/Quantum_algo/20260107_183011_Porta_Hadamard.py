# Este código demonstra a aplicação da porta Hadamard em computação quântica usando a biblioteca Qiskit. 
# A porta Hadamard cria uma superposição a partir do estado |0⟩, resultando em uma combinação igual de |0⟩ e |1⟩. 
# Para executar este código, instale o Qiskit com o comando: pip install qiskit

from qiskit import QuantumCircuit, Aer, execute

# Cria um circuito quântico com 1 qubit
circuit = QuantumCircuit(1)

# Aplica a porta Hadamard ao qubit
circuit.h(0)

# Mede o qubit
circuit.measure_all()

# Executa o circuito em um simulador
simulator = Aer.get_backend('aer_simulator')
result = execute(circuit, backend=simulator, shots=1000).result()

# Obtém e imprime os resultados
counts = result.get_counts(circuit)
print(counts)