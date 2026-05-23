# O método de interpolação de Newton utiliza diferenças divididas para construir um polinômio que passa por um conjunto de pontos.
# A forma de Newton é expressa como um polinômio que pode ser facilmente avaliado e atualizado com novos pontos.
# A fórmula geral do polinômio interpolador de Newton é dada por:
# P(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + ... + f[x_0, x_1, ..., x_n](x - x_0)(x - x_1)...(x - x_{n-1}),
# onde f[x_i] são os valores da função nos pontos x_i e f[x_i, x_j] são as diferenças divididas.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def diferencias_divididas(x, y):
    """
    Calcula a tabela de diferenças divididas.
    
    Parameters:
    x : list
        Lista de valores de x.
    y : list
        Lista de valores de y correspondentes.
        
    Returns:
    coef : np.ndarray
        Vetor de coeficientes das diferenças divididas.
    """
    n = len(y)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    
    return coef[0]

def polinomio_newton(x, coef):
    """
    Constrói o polinômio de Newton a partir dos coeficientes de diferenças divididas.
    
    Parameters:
    x : list
        Lista de valores de x.
    coef : np.ndarray
        Vetor de coeficientes das diferenças divididas.
        
    Returns:
    P : sympy expression
        Expressão simbólica do polinômio de Newton.
    """
    X = sp.symbols('X')
    n = len(coef)
    P = coef[0]
    produto = 1
    
    for i in range(1, n):
        produto *= (X - x[i - 1])
        P += coef[i] * produto
    
    return P

# Exemplo numérico
x = [0, 1, 2, 3]
y = [1, 2, 0, 5]

# Cálculo das diferenças divididas
coef = diferencias_divididas(x, y)

# Construção do polinômio de Newton
P = polinomio_newton(x, coef)

# Impressão do polinômio em LaTeX
sp.init_printing()
display(P)

# Avaliação do polinômio em um intervalo
x_vals = np.linspace(-1, 4, 100)
P_func = sp.lambdify(sp.symbols('X'), P, 'numpy')
y_vals = P_func(x_vals)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Polinômio de Newton', color='blue')
plt.scatter(x, y, color='red', label='Pontos dados')
plt.title('Interpolação de Newton')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid()
plt.show()