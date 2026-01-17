# O plano tangente a uma superfície em um ponto é uma aproximação linear da superfície nesse ponto. 
# A equação do plano tangente é dada por z = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b), 
# onde f_x e f_y são as derivadas parciais de f em relação a x e y, respectivamente. 
# Neste script, vamos calcular e visualizar o plano tangente para uma função de duas variáveis.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializando a impressão em LaTeX
sp.init_printing()

def plano_tangente(funcao, ponto):
    """
    Calcula a equação do plano tangente de uma função em um ponto específico.

    :param funcao: Função de duas variáveis (sympy).
    :param ponto: Tupla com as coordenadas (x, y) do ponto de tangência.
    :return: Equação do plano tangente (sympy).
    """
    x, y = sp.symbols('x y')
    z = funcao
    # Calculando as derivadas parciais
    f_x = sp.diff(z, x).subs({x: ponto[0], y: ponto[1]})
    f_y = sp.diff(z, y).subs({x: ponto[0], y: ponto[1]})
    
    # Valor da função no ponto
    z0 = funcao.subs({x: ponto[0], y: ponto[1]})
    
    # Equação do plano tangente
    plano = z0 + f_x * (x - ponto[0]) + f_y * (y - ponto[1])
    return plano

def plotar_plano_tangente(funcao, ponto):
    """
    Plota a função e o seu plano tangente em um gráfico 3D.

    :param funcao: Função de duas variáveis (sympy).
    :param ponto: Tupla com as coordenadas (x, y) do ponto de tangência.
    """
    x, y = sp.symbols('x y')
    z = funcao

    # Criando a grade de pontos
    x_vals = np.linspace(-2, 2, 100)
    y_vals = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    # Avaliando a função original
    Z = sp.lambdify((x, y), z, 'numpy')(X, Y)
    
    # Calculando o plano tangente
    plano = plano_tangente(funcao, ponto)
    Z_tangente = sp.lambdify((x, y), plano, 'numpy')(X, Y)

    # Plotando
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Superfície original
    ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='blue', label='Superfície f(x, y)')
    
    # Superfície do plano tangente
    ax.plot_surface(X, Y, Z_tangente, alpha=0.5, rstride=100, cstride=100, color='red', label='Plano Tangente')
    
    # Ponto de tangência
    z0 = funcao.subs({x: ponto[0], y: ponto[1]})
    ax.scatter(ponto[0], ponto[1], z0, color='black', s=100)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Função e seu Plano Tangente')
    plt.show()

# Definindo a função
x, y = sp.symbols('x y')
funcao = sp.sin(sp.sqrt(x**2 + y**2))

# Ponto de tangência
ponto_tangente = (1, 1)

# Calculando e exibindo a equação do plano tangente
plano = plano_tangente(funcao, ponto_tangente)
sp.pretty_print(plano)

# Plotando a função e o plano tangente
plotar_plano_tangente(funcao, ponto_tangente)