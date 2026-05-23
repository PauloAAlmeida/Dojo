# A Segunda Forma Fundamental de uma superfície fornece informações sobre a curvatura da superfície em um ponto. 
# Ela é definida em termos das derivadas parciais da parametrização da superfície e do vetor normal. 
# A curvatura gaussiana e a curvatura média são conceitos importantes que podem ser derivados a partir da Segunda Forma Fundamental.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Matrix, Function, diff, simplify, init_printing
from scipy.optimize import minimize

# Inicializa a impressão do LaTeX
init_printing()

# Definindo a superfície como uma função paramétrica
def surface(u, v):
    """Define a superfície z = f(x, y) = x^2 + y^2."""
    return u**2 + v**2

# Calcula as derivadas parciais da superfície
def partial_derivatives(u, v):
    """Calcula as derivadas parciais da superfície."""
    x, y = symbols('x y')
    z = surface(x, y)
    dz_dx = diff(z, x)
    dz_dy = diff(z, y)
    return dz_dx.subs({x: u, y: v}), dz_dy.subs({x: u, y: v})

# Calcula a matriz da Segunda Forma Fundamental
def second_fundamental_form(u, v):
    """Calcula a Segunda Forma Fundamental em um ponto (u, v)."""
    dz_dx, dz_dy = partial_derivatives(u, v)
    N = Matrix([-dz_dx, -dz_dy, 1]).normalized()  # Vetor normal
    E = 1 + dz_dx**2  # E
    F = dz_dx * dz_dy  # F
    G = 1 + dz_dy**2  # G
    L = diff(dz_dx, u)  # L
    M = diff(dz_dy, v)  # M
    N = diff(1, u)  # N
    II = Matrix([[L, M], [M, N]])  # Segunda Forma Fundamental
    return II, E, F, G

# Calcula a curvatura gaussiana e média
def curvature(u, v):
    """Calcula a curvatura gaussiana e média a partir da Segunda Forma Fundamental."""
    II, E, F, G = second_fundamental_form(u, v)
    K = II.det() / (E * G - F**2)  # Curvatura Gaussiana
    H = (II[0, 0] + II[1, 1]) / 2  # Curvatura Média
    return K, H

# Função para visualizar a superfície
def plot_surface():
    """Plota a superfície e suas curvas de nível."""
    u = np.linspace(-2, 2, 100)
    v = np.linspace(-2, 2, 100)
    U, V = np.meshgrid(u, v)
    Z = surface(U, V)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(U, V, Z, cmap='viridis', alpha=0.7)
    ax.set_xlabel('U')
    ax.set_ylabel('V')
    ax.set_zlabel('Z')
    ax.set_title('Superfície z = u^2 + v^2')
    plt.show()

# Exemplo numérico
u_val, v_val = 1, 1
K, H = curvature(u_val, v_val)
print(f"Curvatura Gaussiana K em (u, v) = ({u_val}, {v_val}): {K}")
print(f"Curvatura Média H em (u, v) = ({u_val}, {v_val}): {H}")

# Visualiza a superfície
plot_surface()