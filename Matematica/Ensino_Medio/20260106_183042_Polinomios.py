# O Teorema do Resto afirma que, dado um polinômio P(x) e um número real a, o resto da divisão de P(x) por (x - a) é igual a P(a).
# Isso implica que se P(a) = 0, então a é uma raiz do polinômio. 
# Vamos explorar este teorema, realizar divisões de polinômios e encontrar raízes utilizando Python.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inicializa a impressão em LaTeX
sp.init_printing()

def teorema_do_resto(polinomio, a):
    """
    Calcula o resto da divisão de um polinômio P(x) por (x - a) usando o Teorema do Resto.
    
    Parameters:
    polinomio (sympy Poly): O polinômio a ser avaliado.
    a (float): O valor em que o polinômio será avaliado.
    
    Returns:
    float: O resto da divisão.
    """
    resto = polinomio.eval(a)
    return resto

def divisao_polinomios(polinomio, divisor):
    """
    Realiza a divisão de um polinômio P(x) por um divisor (x - a) e retorna o quociente e o resto.
    
    Parameters:
    polinomio (sympy Poly): O polinômio a ser dividido.
    divisor (sympy Poly): O divisor do polinômio.
    
    Returns:
    tuple: Quociente e resto da divisão.
    """
    quociente, resto = sp.div(polinomio, divisor)
    return quociente, resto

def encontrar_raizes(polinomio):
    """
    Encontra as raízes de um polinômio usando o método de Newton.
    
    Parameters:
    polinomio (sympy Poly): O polinômio cujas raízes serão encontradas.
    
    Returns:
    list: Lista de raízes encontradas.
    """
    return sp.solve(polinomio, sp.Symbol('x'))

# Definindo um polinômio P(x) = x^3 - 6x^2 + 11x - 6
x = sp.Symbol('x')
polinomio = x**3 - 6*x**2 + 11*x - 6

# Aplicando o Teorema do Resto
a = 2
resto = teorema_do_resto(polinomio, a)
print(f"O resto da divisão de P(x) por (x - {a}) é: {resto}")

# Dividindo o polinômio por (x - 2)
divisor = x - a
quociente, resto_divisao = divisao_polinomios(polinomio, divisor)
print(f"Quociente: {quociente}, Resto: {resto_divisao}")

# Encontrando as raízes do polinômio
raizes = encontrar_raizes(polinomio)
print(f"As raízes do polinômio são: {raizes}")

# Visualizando o polinômio e suas raízes
x_vals = np.linspace(0, 4, 400)
y_vals = [polinomio.subs(x, val) for val in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='P(x) = x^3 - 6x^2 + 11x - 6', color='blue')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')

# Plotando as raízes
for raiz in raizes:
    plt.plot(float(raiz), 0, 'ro')  # Raízes em vermelho
    plt.text(float(raiz), 0.5, f'Raiz: {raiz}', fontsize=9, ha='center')

plt.title('Gráfico do Polinômio e suas Raízes')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid()
plt.legend()
plt.show()