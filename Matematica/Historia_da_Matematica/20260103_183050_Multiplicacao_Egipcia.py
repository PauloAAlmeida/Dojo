# A multiplicação egípcia, também conhecida como o método de duplicação ou multiplicação russa, é um método antigo de multiplicação que não utiliza a notação algébrica moderna. 
# Este método remonta ao Antigo Egito, onde os matemáticos usavam tabelas e duplicações para realizar multiplicações. 
# A genialidade desse método reside na sua simplicidade e eficiência, permitindo calcular produtos sem a necessidade de operações complexas. 
# Neste script, vamos implementar a multiplicação egípcia e compará-la com o método moderno, além de visualizar os conceitos geometricamente e simbolicamente.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, init_printing

init_printing()

def multiplicacao_egipcia(a, b):
    """
    Executa a multiplicação egípcia (método de duplicação).
    
    Args:
        a (int): O primeiro número.
        b (int): O segundo número.
        
    Returns:
        int: O resultado da multiplicação.
    """
    resultado = 0
    passos = []  # Para armazenar os passos da multiplicação
    
    while b > 0:
        if b % 2 == 1:  # Se b é ímpar
            resultado += a
            passos.append((a, b, resultado))
        a *= 2  # Duplicar a
        b //= 2  # Dividir b por 2
    
    return resultado, passos

def multiplicacao_moderno(a, b):
    """
    Executa a multiplicação moderna usando o operador de multiplicação.
    
    Args:
        a (int): O primeiro número.
        b (int): O segundo número.
        
    Returns:
        int: O resultado da multiplicação.
    """
    return a * b

def visualizar_passos(passos):
    """
    Visualiza os passos da multiplicação egípcia.
    
    Args:
        passos (list): Lista de tuplas contendo os passos da multiplicação.
    """
    a_vals = [p[0] for p in passos]
    b_vals = [p[1] for p in passos]
    resultados = [p[2] for p in passos]
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(passos)), a_vals, label='Valores de a (duplicação)', marker='o')
    plt.plot(range(len(passos)), b_vals, label='Valores de b (divisão)', marker='o')
    plt.plot(range(len(passos)), resultados, label='Resultados parciais', marker='o')
    
    plt.title('Visualização dos Passos da Multiplicação Egípcia')
    plt.xlabel('Passo')
    plt.ylabel('Valores')
    plt.xticks(range(len(passos)))
    plt.legend()
    plt.grid()
    plt.show()

# Exemplo de uso
a = 18
b = 23

resultado_egipcio, passos = multiplicacao_egipcia(a, b)
resultado_moderno = multiplicacao_moderno(a, b)

print(f"Resultado da multiplicação egípcia de {a} e {b}: {resultado_egipcio}")
print(f"Resultado da multiplicação moderna de {a} e {b}: {resultado_moderno}")

visualizar_passos(passos)

# Demonstração simbólica com SymPy
x, y = symbols('x y')
eq = Eq(x * y, resultado_moderno)
solucao = solve(eq, x)
display(solucao)