# A quadratura adaptativa é um método numérico utilizado para calcular integrais definidas de forma eficiente. 
# O método ajusta automaticamente a subdivisão do intervalo de integração, controlando o erro estimado. 
# A ideia é dividir o intervalo em subintervalos menores onde a função apresenta maior complexidade, 
# utilizando uma regra de quadratura simples, como a regra do trapézio ou Simpson.
# Neste script, utilizaremos a biblioteca SymPy para manipulação simbólica, 
# NumPy para computação numérica, SciPy para métodos numéricos e Matplotlib para visualizações.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sp

# Inicializa a impressão de resultados em LaTeX
sp.init_printing()

def f(x):
    """Função a ser integrada."""
    return np.sin(x) ** 2

def adaptive_quadrature(func, a, b, tol):
    """
    Realiza a quadratura adaptativa de uma função em um intervalo [a, b].
    
    Parameters:
    func : callable
        A função a ser integrada.
    a : float
        Limite inferior do intervalo.
    b : float
        Limite superior do intervalo.
    tol : float
        Tolerância para controle de erro.
    
    Returns:
    float
        O valor aproximado da integral.
    """
    # Cálculo da integral usando a regra do trapézio
    def trapezoidal_rule(f, a, b):
        return (b - a) * (f(a) + f(b)) / 2

    # Cálculo da integral em dois subintervalos
    mid = (a + b) / 2
    I1 = trapezoidal_rule(func, a, b)
    I2 = trapezoidal_rule(func, a, mid) + trapezoidal_rule(func, mid, b)
    
    # Controle de erro
    if np.abs(I2 - I1) < tol:
        return I2
    else:
        # Recursão nos subintervalos
        return adaptive_quadrature(func, a, mid, tol) + adaptive_quadrature(func, mid, b, tol)

# Definindo os limites de integração e a tolerância
a, b = 0, np.pi
tolerance = 1e-6

# Calculando a integral adaptativa
integral_value = adaptive_quadrature(f, a, b, tolerance)

# Exibindo o resultado
print(f"O valor aproximado da integral de sin^2(x) de {a} a {b} é: {integral_value:.6f}")

# Visualização da função
x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label=r'$f(x) = \sin^2(x)$', color='blue')
plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue')
plt.title('Visualização da Função a Ser Integrada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()

# Demonstração simbólica da integral usando SymPy
x = sp.symbols('x')
integral_sym = sp.integrate(sp.sin(x)**2, (x, a, b))
integral_sym_value = integral_sym.evalf()

# Exibindo o resultado simbólico
display(integral_sym)
print(f"O valor exato da integral de sin^2(x) de {a} a {b} é: {integral_sym_value:.6f}")