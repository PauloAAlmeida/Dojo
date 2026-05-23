"""
O gradiente de uma função escalar é um vetor que aponta na direção de máximo crescimento da função. 
Matematicamente, o gradiente é definido como o vetor das derivadas parciais da função em relação a cada uma de suas variáveis. 
Neste script, exploraremos o conceito de gradiente, calcularemos o gradiente de uma função de duas variáveis 
e visualizaremos a direção de máximo crescimento usando gráficos.
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializa a impressão em LaTeX
sp.init_printing()

def calcular_gradiente(funcao, variaveis):
    """
    Calcula o gradiente de uma função escalar.

    Args:
        funcao: A função escalar para a qual o gradiente será calculado.
        variaveis: Uma lista de variáveis independentes da função.

    Returns:
        Um vetor contendo as derivadas parciais da função em relação a cada variável.
    """
    gradiente = [sp.diff(funcao, var) for var in variaveis]
    return gradiente

def visualizar_gradiente(funcao, variaveis, ponto, delta=0.1):
    """
    Visualiza a função e o gradiente em um ponto específico.

    Args:
        funcao: A função escalar a ser visualizada.
        variaveis: Uma lista de variáveis independentes da função.
        ponto: Um tuple representando as coordenadas (x, y) do ponto de interesse.
        delta: O tamanho do passo para o vetor gradiente.
    """
    x, y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
    z = sp.lambdify(variaveis, funcao, 'numpy')(x, y)

    plt.figure(figsize=(10, 8))
    plt.contourf(x, y, z, levels=50, cmap='viridis')
    plt.colorbar(label='Valor da função')
    
    # Calcula o gradiente no ponto
    gradiente = calcular_gradiente(funcao, variaveis)
    gradiente_num = [float(g.subs({variaveis[0]: ponto[0], variaveis[1]: ponto[1]})) for g in gradiente]
    
    # Plota o vetor gradiente
    plt.quiver(ponto[0], ponto[1], gradiente_num[0], gradiente_num[1], 
               color='red', angles='xy', scale_units='xy', scale=1, label='Gradiente')
    
    plt.scatter(*ponto, color='blue', s=100, label='Ponto de interesse')
    plt.title('Visualização do Gradiente')
    plt.xlabel(variaveis[0])
    plt.ylabel(variaveis[1])
    plt.legend()
    plt.grid()
    plt.show()

# Definindo a função e as variáveis
x, y = sp.symbols('x y')
funcao = x**2 + y**2  # Exemplo de função: f(x, y) = x^2 + y^2

# Calculando e exibindo o gradiente simbolicamente
gradiente = calcular_gradiente(funcao, [x, y])
display(sp.Matrix(gradiente))

# Visualizando o gradiente em um ponto específico
visualizar_gradiente(funcao, [x, y], ponto=(1, 1))