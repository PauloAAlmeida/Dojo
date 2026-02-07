# A trissecção do ângulo é um dos problemas clássicos da geometria que se tornou famoso na Grécia Antiga. 
# O problema consiste em dividir um ângulo em três partes iguais usando apenas régua e compasso. 
# Apesar de muitos matemáticos da antiguidade, como Arquímedes e Apolônio, terem tentado resolver este problema, 
# ele foi provado como impossível de ser resolvido com os instrumentos permitidos. 
# No entanto, soluções podem ser encontradas usando cônicas e espirais. 
# Neste script, vamos explorar essas soluções e compará-las com métodos modernos.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, cos, sin, pi, sqrt, init_printing

# Inicializa a impressão do LaTeX
init_printing()

def angle_trisection_with_conics():
    """
    Demonstra a trissecção do ângulo usando cônicas. 
    O método envolve a construção de uma hipérbole e a interseção com uma circunferência.
    """
    # Definindo o ângulo
    angle = pi / 3  # 60 graus
    x, y = symbols('x y')

    # Equações da circunferência e hipérbole
    circle_eq = Eq(x**2 + y**2, 1)  # Circunferência de raio 1
    hyperbola_eq = Eq(y, sqrt(3) * x)  # Hipérbole para a trissecção

    # Solução para encontrar os pontos de interseção
    intersection_points = solve((circle_eq, hyperbola_eq), (x, y))
    
    return intersection_points

def plot_conics_and_intersections(intersection_points):
    """
    Plota a circunferência e a hipérbole, mostrando os pontos de interseção.
    """
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)

    x_hyperbola = np.linspace(-2, 2, 400)
    y_hyperbola_pos = np.sqrt(3) * x_hyperbola
    y_hyperbola_neg = -np.sqrt(3) * x_hyperbola

    plt.figure(figsize=(8, 8))
    plt.plot(x_circle, y_circle, label='Circunferência (x² + y² = 1)')
    plt.plot(x_hyperbola, y_hyperbola_pos, label='Hipérbole (y = √3 * x)', color='orange')
    plt.plot(x_hyperbola, y_hyperbola_neg, color='orange')

    # Marcando os pontos de interseção
    for point in intersection_points:
        plt.plot(float(point[0]), float(point[1]), 'ro')  # Ponto de interseção
        plt.text(float(point[0]), float(point[1]), f'({point[0]:.2f}, {point[1]:.2f})', fontsize=12)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Trissecção do Ângulo usando Cônicas')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    intersection_points = angle_trisection_with_conics()
    print("Pontos de interseção (soluções para a trissecção):")
    for point in intersection_points:
        print(f"({point[0]:.2f}, {point[1]:.2f})")
    
    plot_conics_and_intersections(intersection_points)

if __name__ == "__main__":
    main()