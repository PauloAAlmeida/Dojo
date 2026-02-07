# Este script demonstra a fatoração de polinômios usando Python. 
# A fatoração é o processo de decompor um polinômio em produtos de polinômios de grau inferior. 
# Isso é útil para resolver equações polinomiais e entender as raízes de funções. 
# Utilizaremos a biblioteca SymPy para manipulação simbólica e a Matplotlib para visualizações.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inicializa a impressão em LaTeX
sp.init_printing()

def fatorar_polinomio(expr):
    """
    Fatora um polinômio dado uma expressão simbólica.

    Args:
        expr (sympy.Expr): A expressão simbólica do polinômio a ser fatorado.

    Returns:
        sympy.Expr: O polinômio fatorado.
    """
    return sp.factor(expr)

def visualizar_polinomio(expr, x_range):
    """
    Plota o gráfico de um polinômio.

    Args:
        expr (sympy.Expr): A expressão simbólica do polinômio.
        x_range (tuple): O intervalo de x para plotar (min, max).
    """
    x = np.linspace(x_range[0], x_range[1], 400)
    y = [expr.subs(sp.symbols('x'), val) for val in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=str(expr), color='b')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.title('Gráfico do Polinômio')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend()
    plt.show()

# Exemplo de uso
x = sp.symbols('x')
polinomio = x**3 - 6*x**2 + 11*x - 6

# Fatoração do polinômio
polinomio_fatorado = fatorar_polinomio(polinomio)
print("Polinômio original:")
sp.pprint(polinomio)
print("\nPolinômio fatorado:")
sp.pprint(polinomio_fatorado)

# Visualização do polinômio
visualizar_polinomio(polinomio, (-2, 5))
visualizar_polinomio(polinomio_fatorado, (-2, 5))

# Exemplo numérico
coefficients = [1, -6, 11, -6]  # Coeficientes do polinômio
roots = np.roots(coefficients)
print("\nRaízes do polinômio:", roots)