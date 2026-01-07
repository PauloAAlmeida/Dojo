# Este código implementa um oráculo quântico para uma função booleana simples usando Qiskit. 
# O oráculo irá marcar um estado específico como "solução" em um circuito quântico. 
# Para executar este código, é necessário instalar o Qiskit com o comando: 
# pip install qiskit

from qiskit import QuantumCircuit, Aer, execute

# Definindo a função booleana: f(x) = 1 se x = 11 (em binário), caso contrário f(x) = 0
def oracle(circuit):
    circuit.x(0)  # Inverte o qubit 0
    circuit.x(1)  # Inverte o qubit 1
    circuit.ccx(0, 1, 2)  # Porta Toffoli
    circuit.x(0)  # Restaura o qubit 0
    circuit.x(1)  # Restaura o qubit 1

# Criando o circuito quântico
qc = QuantumCircuit(3, 2)  # 2 qubits de entrada e 1 qubit de saída
qc.h([0, 1])  # Colocando os qubits em superposição
oracle(qc)  # Aplicando o oráculo
qc.h([0, 1])  # Aplicando Hadamard novamente
qc.measure([0, 1], [0, 1])  # Medindo os qubits

# Executando o circuito
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts()

# Imprimindo os resultados
print("Resultados da medição:", counts)