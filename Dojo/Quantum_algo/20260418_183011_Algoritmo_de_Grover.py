# Este código demonstra o algoritmo de Grover, que é utilizado para buscar um item específico em um banco de dados não estruturado de forma eficiente. O algoritmo reduz o número de consultas necessárias em comparação com uma busca clássica. Para executar este código, instale o Qiskit com o comando: pip install qiskit

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
import numpy as np

def grover_circuit(target):
    n = len(target)
    qc = QuantumCircuit(n)
    
    # Inicialização
    qc.h(range(n))
    
    # Oracle
    for i in range(n):
        if target[i] == '0':
            qc.x(i)
    qc.h(n-1)
    qc.mct(list(range(n-1)), n-1)  # Multi-controlled Toffoli
    qc.h(n-1)
    for i in range(n):
        if target[i] == '0':
            qc.x(i)
    
    # Difusão
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mct(list(range(n-1)), n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    
    return qc

# Definindo o alvo
target = '11'  # O item que estamos procurando
qc = grover_circuit(target)
qc = transpile(qc, optimization_level=3)
simulator = Aer.get_backend('aer_simulator')
qobj = assemble(qc)
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts()

# Exibindo os resultados
print("Resultados da busca:", counts)