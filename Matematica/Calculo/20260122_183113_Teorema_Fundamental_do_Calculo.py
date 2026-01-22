# O Teorema Fundamental do Cálculo conecta a derivação e a integração, duas operações fundamentais do cálculo. 
# Ele consiste em duas partes: a primeira parte afirma que se uma função é contínua em um intervalo fechado e 
# possui uma primitiva, então a integral definida dessa função pode ser calculada usando essa primitiva. 
# A segunda parte afirma que a derivada da integral de uma função é a própria função. 
# Este script demonstrará essas duas partes usando a biblioteca SymPy para manipulação simbólica e Matplotlib para visualizações.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializa a impressão de resultados em LaTeX
sp.init_printing()

def primeira_parte_teorema_fundamental(funcao, a, b):
    """
    Demonstra a primeira parte do Teorema Fundamental do Cálculo.
    
    Parameters:
    funcao (sympy expression): A função a ser integrada.
    a (float): Limite inferior da integral.
    b (float): Limite superior da integral.
    
    Returns:
    float: Valor da integral definida da função no intervalo [a, b].
    """
    F = sp.integrate(funcao, sp.Symbol('x'))  # Calcula a primitiva
    integral = F.subs(sp.Symbol('x'), b) - F.subs(sp.Symbol('x'), a)  # Integral definida
    return integral, F

def segunda_parte_teorema_fundamental(funcao):
    """
    Demonstra a segunda parte do Teorema Fundamental do Cálculo.
    
    Parameters:
    funcao (sympy expression): A função a ser derivada.
    
    Returns:
    sympy expression: A derivada da integral da função.
    """
    x = sp.Symbol('x')
    F = sp.integrate(funcao, x)  # Integral indefinida
    derivada = sp.diff(F, x)  # Derivada da integral
    return derivada

# Definindo uma função para as demonstrações
x = sp.Symbol('x')
funcao = sp.sin(x)  # Função a ser utilizada

# Demonstração da primeira parte
a, b = 0, np.pi  # Limites da integral
integral_resultado, primitiva = primeira_parte_teorema_fundamental(funcao, a, b)
print(f"Integral definida de sin(x) de {a} a {b}: {integral_resultado}")
print(f"Primitiva de sin(x): {primitiva}")

# Demonstração da segunda parte
derivada_resultado = segunda_parte_teorema_fundamental(funcao)
print(f"Derivada da integral de sin(x): {derivada_resultado}")

# Visualização da função e sua primitiva
x_vals = np.linspace(-1, 2 * np.pi, 100)
y_vals = np.sin(x_vals)
primitiva_func = -np.cos(x_vals) + 1  # Primitiva de sin(x) é -cos(x) + C

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, label='sin(x)', color='blue')
plt.title('Função: sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_vals, primitiva_func, label='Primitiva: -cos(x) + C', color='orange')
plt.title('Primitiva de sin(x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()

plt.tight_layout()
plt.show()