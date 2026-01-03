# Este código demonstra o algoritmo de Grover, que é utilizado para buscar um item em uma lista não ordenada de forma eficiente. O algoritmo amplifica a amplitude do estado correspondente ao item buscado, permitindo encontrá-lo em um número reduzido de passos em comparação com uma busca clássica. Para executar este código, instale a biblioteca Qiskit com o comando: pip install qiskit.

from qiskit import QuantumCircuit, Aer, execute

def grover_circuit(n, marked_index):
    # Criar um circuito quântico com n qubits
    circuit = QuantumCircuit(n)
    
    # Inicializar os qubits em superposição
    circuit.h(range(n))
    
    # Aplicar a operação de oracle
    for i in range(n):
        if i == marked_index:
            circuit.z(i)
    
    # Amplificação de amplitude
    circuit.h(range(n))
    circuit.x(range(n))
    circuit.h(n-1)
    circuit.mct(list(range(n-1)), n-1)  # Porta de controle múltiplo
    circuit.h(n-1)
    circuit.x(range(n))
    circuit.h(range(n))
    
    return circuit

# Parâmetros
n = 3  # Número de qubits
marked_index = 1  # Índice do item marcado

# Criar e executar o circuito
grover = grover_circuit(n, marked_index)
backend = Aer.get_backend('statevector_simulator')
result = execute(grover, backend).result()
statevector = result.get_statevector()

# Exibir o resultado
print("Statevector:", statevector)