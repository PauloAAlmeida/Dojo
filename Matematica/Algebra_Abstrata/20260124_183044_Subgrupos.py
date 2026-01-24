# Este script explora o conceito de subgrupos em álgebra abstrata. 
# Um subgrupo H de um grupo G é um conjunto não vazio que é fechado sob a operação do grupo e contém o inverso de cada um de seus elementos. 
# O critério do subgrupo fornece uma maneira de verificar se um subconjunto é um subgrupo. 
# O reticulado de subgrupos é uma estrutura que organiza todos os subgrupos de um grupo em uma relação de inclusão.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def init_sympy_printing():
    """Inicializa a impressão do SymPy para LaTeX."""
    sp.init_printing(use_unicode=True)

def is_subgroup(G, H):
    """
    Verifica se H é um subgrupo de G usando o critério do subgrupo.
    
    Parâmetros:
    G : list
        O grupo original.
    H : list
        O subconjunto a ser verificado.
    
    Retorna:
    bool
        True se H é um subgrupo de G, False caso contrário.
    """
    if not H:  # H deve ser não vazio
        return False
    if not all(h in G for h in H):  # H deve estar contido em G
        return False
    # Verifica se a operação é fechada em H
    for a in H:
        for b in H:
            if (a * b) not in H:
                return False
    # Verifica se o inverso de cada elemento está em H
    for h in H:
        if (h**-1) not in H:
            return False
    return True

def generate_subgroup_examples(G):
    """
    Gera exemplos de subgrupos a partir de um grupo G.
    
    Parâmetros:
    G : list
        O grupo original.
    
    Retorna:
    list
        Lista de subgrupos encontrados.
    """
    subgroups = []
    for i in range(1, len(G)+1):
        for subset in combinations(G, i):
            if is_subgroup(G, list(subset)):
                subgroups.append(set(subset))
    return subgroups

def plot_lattice_of_subgroups(subgroups):
    """
    Plota o reticulado de subgrupos usando NetworkX.
    
    Parâmetros:
    subgroups : list
        Lista de subgrupos a serem plotados.
    """
    G = nx.DiGraph()
    for subgroup in subgroups:
        G.add_node(f"{subgroup}")
    
    for i, subgroup1 in enumerate(subgroups):
        for subgroup2 in subgroups:
            if subgroup1 < subgroup2:  # se subgroup1 é um subconjunto de subgroup2
                G.add_edge(f"{subgroup1}", f"{subgroup2}")
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True)
    plt.title("Reticulado de Subgrupos")
    plt.show()

# Exemplo numérico
G = [1, 2, 3, 4]  # Um grupo exemplo, considerando a multiplicação módulo 5
H = [1, 2]  # Um subconjunto a ser verificado

init_sympy_printing()
print(f"Verificando se H = {H} é um subgrupo de G = {G}: {is_subgroup(G, H)}")

# Gerar exemplos de subgrupos
from itertools import combinations
subgroups = generate_subgroup_examples(G)
print("Subgrupos encontrados:", subgroups)

# Plotar o reticulado de subgrupos
plot_lattice_of_subgroups(subgroups)