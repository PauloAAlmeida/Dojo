# O Teorema da Soma de Quatro Quadrados, proposto por Joseph-Louis Lagrange, afirma que
# todo número inteiro não negativo pode ser expresso como a soma de quatro quadrados inteiros.
# Em outras palavras, para qualquer número inteiro n >= 0, existem inteiros a, b, c e d tais que:
# n = a^2 + b^2 + c^2 + d^2. Este teorema é um resultado fundamental na teoria dos números
# e tem várias aplicações em diferentes áreas da matemática.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inicializa a impressão do SymPy para LaTeX
sp.init_printing()

def lagrange_four_squares(n):
    """
    Encontra inteiros a, b, c e d tais que n = a^2 + b^2 + c^2 + d^2.
    
    Parâmetros:
    n (int): O número inteiro não negativo a ser decomposto.
    
    Retorna:
    tuple: Uma tupla contendo os inteiros (a, b, c, d).
    """
    for a in range(int(np.sqrt(n)) + 1):
        for b in range(int(np.sqrt(n - a**2)) + 1):
            for c in range(int(np.sqrt(n - a**2 - b**2)) + 1):
                d_squared = n - a**2 - b**2 - c**2
                if d_squared >= 0:
                    d = int(np.sqrt(d_squared))
                    if d**2 == d_squared:
                        return a, b, c, d
    return None

def demonstrate_lagrange_theorem(n):
    """
    Demonstra o Teorema da Soma de Quatro Quadrados para um número inteiro n.
    
    Parâmetros:
    n (int): O número inteiro não negativo a ser decomposto.
    """
    a, b, c, d = lagrange_four_squares(n)
    if (a, b, c, d) is not None:
        print(f"O número {n} pode ser expresso como a soma de quadrados:")
        print(f"{n} = {a}^2 + {b}^2 + {c}^2 + {d}^2")
        
        # Demonstração simbólica
        x, y, z, w = sp.symbols('x y z w')
        equation = sp.Eq(n, x**2 + y**2 + z**2 + w**2)
        display_equation = equation.subs({x: a, y: b, z: c, w: d})
        sp.display(display_equation)
    else:
        print(f"O número {n} não pode ser expresso como a soma de quatro quadrados.")

def plot_four_squares(n):
    """
    Plota os quadrados dos inteiros que somam para n.
    
    Parâmetros:
    n (int): O número inteiro não negativo a ser decomposto.
    """
    a, b, c, d = lagrange_four_squares(n)
    if (a, b, c, d) is not None:
        squares = [a**2, b**2, c**2, d**2]
        labels = [f'{a}^2', f'{b}^2', f'{c}^2', f'{d}^2']
        
        plt.figure(figsize=(8, 6))
        plt.bar(labels, squares, color='skyblue')
        plt.title(f'Soma de Quadrados para {n}')
        plt.ylabel('Valor dos Quadrados')
        plt.xlabel('Quadrados Inteiros')
        plt.axhline(y=n, color='r', linestyle='--', label='Soma Total')
        plt.legend()
        plt.show()

# Exemplo de uso
n = 29
demonstrate_lagrange_theorem(n)
plot_four_squares(n)