# Este script explora o conceito de extensões de corpos em álgebra abstrata, focando no grau da extensão e na construção de torres de extensões. 
# Uma extensão de corpo é uma maneira de construir novos corpos a partir de corpos existentes, e o grau da extensão é uma medida da "dimensão" da nova extensão em relação ao corpo base. 
# A torre de extensões é uma sequência de extensões onde cada extensão é construída a partir da anterior. 
# Usaremos a biblioteca SymPy para manipulações simbólicas, NumPy para cálculos numéricos e Matplotlib para visualizações.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import init_printing

# Inicializa a impressão em LaTeX
init_printing()

def grau_extensao(corpo_base, corpo_extensao):
    """
    Calcula o grau de uma extensão de corpo.
    
    Parâmetros:
    corpo_base (str): O corpo base (ex: 'Q' para números racionais).
    corpo_extensao (str): O corpo de extensão (ex: 'Q(sqrt(2))').
    
    Retorna:
    int: O grau da extensão.
    """
    base = sp.GF(corpo_base)
    ext = sp.GF(corpo_extensao)
    return ext.degree(base)

def torre_extensoes(corpos):
    """
    Calcula o grau total de uma torre de extensões de corpos.
    
    Parâmetros:
    corpos (list): Lista de corpos na torre.
    
    Retorna:
    int: O grau total da torre.
    """
    grau_total = 1
    for i in range(len(corpos) - 1):
        grau_total *= grau_extensao(corpos[i], corpos[i + 1])
    return grau_total

def visualizar_torre_extensoes(corpos):
    """
    Gera um gráfico da torre de extensões.
    
    Parâmetros:
    corpos (list): Lista de corpos na torre.
    """
    graus = [grau_extensao(corpos[i], corpos[i + 1]) for i in range(len(corpos) - 1)]
    alturas = np.cumsum([0] + graus)
    
    plt.figure(figsize=(8, 5))
    plt.bar(range(len(corpos)), [1] * len(corpos), bottom=alturas, color='skyblue')
    plt.xticks(range(len(corpos)), corpos)
    plt.ylabel('Altura da Torre')
    plt.title('Visualização da Torre de Extensões de Corpos')
    plt.grid(axis='y')
    plt.show()

# Exemplos de uso
corpos = ['Q', 'Q(sqrt(2))', 'Q(sqrt(2), sqrt(3))']

# Cálculo do grau de cada extensão
for i in range(len(corpos) - 1):
    grau = grau_extensao(corpos[i], corpos[i + 1])
    print(f"Grau da extensão {corpos[i]} ⟶ {corpos[i + 1]}: {grau}")

# Cálculo do grau total da torre
grau_total = torre_extensoes(corpos)
print(f"Grau total da torre: {grau_total}")

# Visualização da torre de extensões
visualizar_torre_extensoes(corpos)