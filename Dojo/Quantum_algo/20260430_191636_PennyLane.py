# Este código utiliza a biblioteca PennyLane para demonstrar a computação quântica diferenciável em um problema simples de classificação. 
# Certifique-se de ter o PennyLane instalado. Você pode instalá-lo usando: 
# pip install pennylane pennylane-qiskit
# O código cria um circuito quântico que classifica um ponto em um espaço 2D.

import pennylane as qml
import numpy as np

# Definindo o dispositivo quântico
dev = qml.device("qiskit.aer", wires=2)

@qml.qnode(dev)
def circuit(x):
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(1))

# Dados de entrada (pontos em 2D)
data = np.array([[0.1, 0.2], [0.4, 0.5], [0.9, 0.8]])

# Executando o circuito quântico e imprimindo os resultados
for point in data:
    result = circuit(point)
    print(f"Ponto: {point}, Resultado da Classificação: {result}")