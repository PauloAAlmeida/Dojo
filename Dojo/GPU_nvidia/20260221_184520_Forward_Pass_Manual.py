# Este código demonstra a propagação para frente (forward pass) de uma rede neural simples com uma camada oculta. 
# Ele utiliza apenas bibliotecas padrão do Python, não requer instalação de bibliotecas externas.
# A rede possui uma camada de entrada, uma camada oculta com ativação ReLU e uma camada de saída com ativação sigmoide.
# O código calcula a saída da rede para uma entrada específica.

import numpy as np

# Função de ativação ReLU
def relu(x):
    return np.maximum(0, x)

# Função de ativação sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Pesos e viés da rede
input_size = 2
hidden_size = 2
output_size = 1

# Inicializando pesos e viés aleatórios
np.random.seed(0)
W1 = np.random.rand(input_size, hidden_size)
b1 = np.random.rand(hidden_size)
W2 = np.random.rand(hidden_size, output_size)
b2 = np.random.rand(output_size)

# Entrada da rede
X = np.array([[0.5], [0.8]])

# Forward pass
hidden_layer_input = np.dot(W1.T, X) + b1
hidden_layer_output = relu(hidden_layer_input)
output_layer_input = np.dot(W2.T, hidden_layer_output) + b2
output = sigmoid(output_layer_input)

print("Saída da rede neural:", output)