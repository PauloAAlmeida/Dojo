# Este script explora os conceitos de esperança e variância em estatística. 
# A esperança (ou valor esperado) de uma variável aleatória é uma medida do centro de sua distribuição, 
# enquanto a variância mede a dispersão em relação à média. 
# Usaremos SymPy para manipulações simbólicas, NumPy para cálculos numéricos e Matplotlib para visualizações.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import init_printing

# Inicializa a impressão do SymPy
init_printing()

def esperanca_discreta(valores, probabilidades):
    """
    Calcula a esperança de uma variável aleatória discreta.
    
    :param valores: Lista de valores da variável aleatória.
    :param probabilidades: Lista de probabilidades associadas a cada valor.
    :return: Esperança da variável aleatória.
    """
    return sum(v * p for v, p in zip(valores, probabilidades))

def variancia_discreta(valores, probabilidades):
    """
    Calcula a variância de uma variável aleatória discreta.
    
    :param valores: Lista de valores da variável aleatória.
    :param probabilidades: Lista de probabilidades associadas a cada valor.
    :return: Variância da variável aleatória.
    """
    E_X = esperanca_discreta(valores, probabilidades)
    return sum(p * (v - E_X)**2 for v, p in zip(valores, probabilidades))

def demonstracao_esperanca():
    """
    Demonstra a fórmula da esperança usando SymPy.
    """
    X = sp.symbols('X')
    p = sp.Function('p')(X)
    E_X = sp.integrate(X * p, (X, -sp.oo, sp.oo))
    sp.pprint(E_X)

def demonstracao_variancia():
    """
    Demonstra a fórmula da variância usando SymPy.
    """
    X = sp.symbols('X')
    mu = sp.symbols('mu')
    p = sp.Function('p')(X)
    var_X = sp.integrate((X - mu)**2 * p, (X, -sp.oo, sp.oo))
    sp.pprint(var_X)

# Exemplo numérico
valores = [1, 2, 3, 4, 5]
probabilidades = [0.1, 0.2, 0.3, 0.2, 0.2]

esperanca = esperanca_discreta(valores, probabilidades)
variancia = variancia_discreta(valores, probabilidades)

print(f"Esperança: {esperanca:.2f}")
print(f"Variância: {variancia:.2f}")

# Visualização da distribuição
plt.bar(valores, probabilidades, color='skyblue')
plt.xlabel('Valores')
plt.ylabel('Probabilidades')
plt.title('Distribuição de Probabilidades')
plt.grid(axis='y')
plt.show()

# Demonstrações
print("Demonstração da Esperança:")
demonstracao_esperanca()

print("\nDemonstração da Variância:")
demonstracao_variancia()