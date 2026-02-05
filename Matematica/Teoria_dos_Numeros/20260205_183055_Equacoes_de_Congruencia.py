# Este script explora o conceito de equações de congruência da forma ax ≡ b (mod m).
# As equações de congruência são fundamentais na Teoria dos Números e têm aplicações em criptografia,
# algoritmos e resolução de problemas matemáticos. Vamos usar a biblioteca SymPy para manipulação simbólica,
# NumPy para computação numérica e Matplotlib para visualizações.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, init_printing
from sympy.plotting import plot

# Inicializa a impressão de resultados em LaTeX
init_printing()

def solve_congruence(a, b, m):
    """
    Resolve a equação de congruência ax ≡ b (mod m) e retorna a solução.

    Parameters:
    a (int): Coeficiente da variável x.
    b (int): Constante na equação.
    m (int): Módulo da congruência.

    Returns:
    list: Lista de soluções para a equação de congruência.
    """
    x = symbols('x')
    congruence_eq = Eq(a * x % m, b % m)
    solutions = solve(congruence_eq, x)
    return [sol.evalf() for sol in solutions]

def plot_congruence(a, b, m):
    """
    Plota a função y = ax + b (mod m) para visualizar as soluções da congruência.

    Parameters:
    a (int): Coeficiente da variável x.
    b (int): Constante na equação.
    m (int): Módulo da congruência.
    """
    x_vals = np.arange(0, m)
    y_vals = (a * x_vals + b) % m

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, marker='o')
    plt.title(f'Gráfico de y = ({a}x + {b}) mod {m}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(0, m))
    plt.yticks(np.arange(0, m))
    plt.grid()
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.show()

# Exemplos numéricos
a = 3
b = 4
m = 7

# Resolvendo a congruência
solutions = solve_congruence(a, b, m)
print(f"Soluções da congruência {a}x ≡ {b} (mod {m}): {solutions}")

# Plotando a congruência
plot_congruence(a, b, m)

# Sistema de equações de congruência
def solve_system_congruences(congruences):
    """
    Resolve um sistema de equações de congruência.

    Parameters:
    congruences (list of tuples): Lista de tuplas (a, b, m) representando as equações.

    Returns:
    list: Lista de soluções para o sistema de congruências.
    """
    x = symbols('x')
    equations = [Eq(a * x % m, b % m) for a, b, m in congruences]
    solutions = solve(equations, x)
    return [sol.evalf() for sol in solutions]

# Exemplo de sistema de congruências
congruences = [(2, 3, 5), (3, 4, 7), (1, 1, 3)]
system_solutions = solve_system_congruences(congruences)
print(f"Soluções do sistema de congruências: {system_solutions}")