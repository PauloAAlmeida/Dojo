# Este script explora o conceito de geodésicas em superfícies como a esfera e o cilindro. 
# Geodésicas são as curvas mais curtas entre dois pontos em uma superfície. 
# Neste código, utilizaremos SymPy para manipulação simbólica, NumPy para cálculos numéricos, 
# e Matplotlib para visualizações gráficas. Vamos derivar as equações das geodésicas para uma esfera e um cilindro.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Function, Eq, Matrix, simplify, diff, cos, sin, init_printing
from sympy.calculus.util import minimum

init_printing()

def geodesic_sphere(radius):
    """
    Calcula a geodésica em uma esfera de raio dado.
    
    Parameters:
    radius (float): O raio da esfera.
    
    Returns:
    None: Plota a geodésica na esfera.
    """
    # Definindo variáveis
    theta, phi = symbols('theta phi')
    
    # Parametrização da esfera
    x = radius * sin(phi) * cos(theta)
    y = radius * sin(phi) * sin(theta)
    z = radius * cos(phi)
    
    # Calculando a métrica
    g = Matrix([[radius**2, 0], [0, radius**2 * sin(phi)**2]])
    
    # Calculando a geodésica usando a equação de Euler-Lagrange
    # L = sqrt(g_ij * dx^i/dt * dx^j/dt)
    # Para simplificação, consideramos apenas a parte angular
    L = simplify(g[0, 0] * (diff(x, theta)**2) + g[1, 1] * (diff(y, theta)**2))
    
    # Derivando as equações de Euler-Lagrange
    eq1 = Eq(diff(L, theta) - diff(diff(L, diff(theta)), phi), 0)
    eq2 = Eq(diff(L, phi) - diff(diff(L, diff(phi)), theta), 0)
    
    print("Equações de Euler-Lagrange para a esfera:")
    display(eq1, eq2)

    # Plotando a geodésica
    theta_vals = np.linspace(0, 2 * np.pi, 100)
    phi_vals = np.linspace(0, np.pi, 100)
    X = radius * np.outer(np.sin(phi_vals), np.cos(theta_vals))
    Y = radius * np.outer(np.sin(phi_vals), np.sin(theta_vals))
    Z = radius * np.outer(np.cos(phi_vals), np.ones(np.size(theta_vals)))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, color='b', alpha=0.3)
    ax.set_title('Geodésica na Esfera')
    plt.show()

def geodesic_cylinder(radius, height):
    """
    Calcula a geodésica em um cilindro de raio e altura dados.
    
    Parameters:
    radius (float): O raio do cilindro.
    height (float): A altura do cilindro.
    
    Returns:
    None: Plota a geodésica no cilindro.
    """
    # Definindo variáveis
    theta, z = symbols('theta z')
    
    # Parametrização do cilindro
    x = radius * cos(theta)
    y = radius * sin(theta)
    
    # Calculando a métrica
    g = Matrix([[radius**2, 0], [0, 1]])
    
    # Calculando a geodésica
    L = simplify(g[0, 0] * (diff(x, theta)**2) + g[1, 1] * (diff(z, theta)**2))
    
    # Derivando as equações de Euler-Lagrange
    eq1 = Eq(diff(L, theta) - diff(diff(L, diff(theta)), z), 0)
    eq2 = Eq(diff(L, z) - diff(diff(L, diff(z)), theta), 0)
    
    print("Equações de Euler-Lagrange para o cilindro:")
    display(eq1, eq2)

    # Plotando a geodésica
    theta_vals = np.linspace(0, 2 * np.pi, 100)
    z_vals = np.linspace(0, height, 100)
    X = radius * np.cos(theta_vals)
    Y = radius * np.sin(theta_vals)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X[:, np.newaxis], Y[:, np.newaxis], z_vals[np.newaxis, :], color='r', alpha=0.3)
    ax.set_title('Geodésica no Cilindro')
    plt.show()

# Executando as funções
geodesic_sphere(1)
geodesic_cylinder(1, 2)