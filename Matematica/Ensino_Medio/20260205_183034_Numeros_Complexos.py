# Este script explora os números complexos, suas operações, a forma polar e a fórmula de De Moivre.
# Números complexos são expressões da forma a + bi, onde a e b são números reais e i é a unidade imaginária.
# A forma polar de um número complexo é expressa como r(cos(θ) + i*sin(θ)), onde r é o módulo e θ é o argumento.
# A fórmula de De Moivre permite calcular potências de números complexos na forma polar de maneira eficiente.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, I, cos, sin, sqrt, arg, re, im, exp, pi, init_printing

init_printing()

# Função para calcular a forma polar de um número complexo
def forma_polar(z):
    """
    Calcula a forma polar de um número complexo.
    
    Parameters:
    z (complex): Número complexo.
    
    Returns:
    tuple: Módulo e argumento do número complexo.
    """
    r = abs(z)  # Módulo
    theta = np.angle(z)  # Argumento
    return r, theta

# Função para visualizar números complexos
def plot_complex_numbers(z_list):
    """
    Plota números complexos no plano complexo.
    
    Parameters:
    z_list (list): Lista de números complexos.
    """
    plt.figure(figsize=(8, 8))
    for z in z_list:
        plt.quiver(0, 0, re(z), im(z), angles='xy', scale_units='xy', scale=1)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.title('Números Complexos no Plano')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.show()

# Função para calcular a potência de um número complexo usando a fórmula de De Moivre
def de_moivre(z, n):
    """
    Calcula a potência de um número complexo usando a fórmula de De Moivre.
    
    Parameters:
    z (complex): Número complexo.
    n (int): Expoente.
    
    Returns:
    complex: Resultado da potência.
    """
    r, theta = forma_polar(z)
    r_n = r ** n
    theta_n = n * theta
    return r_n * (cos(theta_n) + I * sin(theta_n))

# Exemplo numérico
z = 1 + 1j  # Número complexo
n = 3  # Expoente

# Cálculo da forma polar
r, theta = forma_polar(z)
print(f'Forma polar de {z}: r = {r:.2f}, θ = {theta:.2f} rad')

# Cálculo da potência usando De Moivre
resultado = de_moivre(z, n)
print(f'{z} elevado a {n} é: {resultado}')

# Visualização
plot_complex_numbers([z, resultado])