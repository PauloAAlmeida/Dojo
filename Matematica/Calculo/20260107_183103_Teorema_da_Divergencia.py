# O Teorema da Divergência, também conhecido como Teorema de Gauss, estabelece uma relação entre o fluxo de um campo vetorial através de uma superfície fechada e a divergência desse campo dentro do volume delimitado pela superfície. 
# Matematicamente, ele pode ser expresso como:
# ∮_S **F** · d**S** = ∫∫∫_V div(**F**) dV
# onde **F** é um campo vetorial, S é a superfície fechada, e V é o volume interno. Este teorema tem aplicações em diversas áreas, como física e engenharia, especialmente em eletromagnetismo e dinâmica de fluidos.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, div, Matrix, init_printing
from sympy.vector import CoordSys3D

init_printing()

# Definindo a função vetorial e a superfície
def vector_field(x, y, z):
    """Define a função vetorial F(x, y, z) = (x^2, y^2, z^2)."""
    return np.array([x**2, y**2, z**2])

# Cálculo da divergência
def calculate_divergence():
    """Calcula a divergência do campo vetorial F."""
    N = CoordSys3D('N')
    F = vector_field(N.x, N.y, N.z)
    divergence = div(Matrix(F), N)
    return divergence

# Cálculo do fluxo através da superfície
def surface_integral():
    """Calcula o fluxo do campo vetorial através da superfície da esfera de raio R."""
    R = symbols('R')
    F = vector_field(R, R, R)
    flux = integrate(F[0] * R**2 * np.sin(np.pi/2) * np.cos(np.pi/2), (R, 0, 1))  # Simplificação para a esfera unitária
    return flux

# Visualização do campo vetorial
def plot_vector_field():
    """Plota o campo vetorial em um espaço 3D."""
    X, Y, Z = np.meshgrid(np.linspace(-1, 1, 5), np.linspace(-1, 1, 5), np.linspace(-1, 1, 5))
    U = X**2
    V = Y**2
    W = Z**2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X, Y, Z, U, V, W, length=0.1, normalize=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Campo Vetorial F(x, y, z) = (x^2, y^2, z^2)')
    plt.show()

# Cálculo e impressão dos resultados
divergence = calculate_divergence()
flux = surface_integral()

print("Divergência do campo vetorial F:")
display(divergence)

print("Fluxo através da superfície da esfera:")
display(flux)

plot_vector_field()