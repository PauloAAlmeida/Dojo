# Este código simula o protocolo BB84 de distribuição de chaves quânticas. 
# O protocolo permite que duas partes compartilhem uma chave secreta de forma segura, 
# utilizando estados quânticos. Para executar este código, você precisará da biblioteca 
# Qiskit. Instale-a usando: pip install qiskit.

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
import numpy as np

def bb84_simulation():
    # Alice escolhe uma base e um bit aleatório
    alice_bits = np.random.randint(2, size=5)
    alice_bases = np.random.randint(2, size=5)

    # Bob escolhe uma base aleatória
    bob_bases = np.random.randint(2, size=5)

    # Criação do circuito quântico
    circuit = QuantumCircuit(5, 5)
    
    for i in range(5):
        if alice_bases[i] == 0:  # Base Z
            if alice_bits[i] == 1:
                circuit.x(i)  # |1> = X |0>
        else:  # Base X
            if alice_bits[i] == 1:
                circuit.x(i)  # |1> = X |0>
                circuit.h(i)   # Aplicar Hadamard

    # Medição de Bob
    for i in range(5):
        if bob_bases[i] == 1:  # Base X
            circuit.h(i)
        circuit.measure(i, i)

    # Execução do circuito
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(circuit, simulator)
    job = execute(compiled_circuit, simulator, shots=1)
    result = job.result()
    measurements = result.get_counts()

    # Comparação das bases e extração da chave
    key = []
    for i in range(5):
        if alice_bases[i] == bob_bases[i]:
            key.append(str(measurements.get('0'*5, 0)))

    print("Alice's bits: ", alice_bits)
    print("Alice's bases: ", alice_bases)
    print("Bob's bases: ", bob_bases)
    print("Shared key: ", ''.join(key))

bb84_simulation()