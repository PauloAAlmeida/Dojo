# Este script explora o conceito de subgrupos em álgebra abstrata, focando no critério de subgrupo e no reticulado de subgrupos.
# Um subgrupo H de um grupo G é um subconjunto que é ele mesmo um grupo sob a operação de G. 
# O critério de subgrupo afirma que um subconjunto H é um subgrupo de G se:
# 1. O elemento neutro de G pertence a H.
# 2. Se a e b estão em H, então a*b^-1 também está em H.
# O reticulado de subgrupos é a estrutura que mostra como os subgrupos se relacionam entre si.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, init_printing
import sympy as sp

init_printing()

def is_subgroup(G, H):
    """
    Verifica se H é um subgrupo de G.
    
    Parâmetros:
    G : list
        Conjunto de elementos do grupo G.
    H : list
        Conjunto de elementos a ser verificado como subgrupo.
        
    Retorna:
    bool
        True se H é um subgrupo de G, False caso contrário.
    """
    # Verifica se o elemento neutro está em H
    identity = G[0]  # Assumindo que o primeiro elemento é o neutro
    if identity not in H:
        return False
    
    # Verifica a condição de fechamento
    for a in H:
        for b in H:
            if (a * b) not in H:
                return False
            if (a * np.linalg.inv(b)) not in H:
                return False
                
    return True

def subgroup_lattice(G):
    """
    Gera o reticulado de subgrupos de um grupo G.
    
    Parâmetros:
    G : list
        Conjunto de elementos do grupo G.
        
    Retorna:
    list
        Lista de subgrupos de G.
    """
    subgroups = []
    for i in range(1, len(G)+1):
        for subset in combinations(G, i):
            if is_subgroup(G, subset):
                subgroups.append(set(subset))
    return subgroups

def visualize_lattice(subgroups):
    """
    Visualiza o reticulado de subgrupos.
    
    Parâmetros:
    subgroups : list
        Lista de subgrupos a serem visualizados.
    """
    plt.figure(figsize=(8, 6))
    for i, subgroup in enumerate(subgroups):
        plt.scatter(i, len(subgroup), label=str(subgroup))
    
    plt.title("Reticulado de Subgrupos")
    plt.xlabel("Subgrupos")
    plt.ylabel("Tamanho do Subgrupo")
    plt.xticks(range(len(subgroups)), [str(s) for s in subgroups], rotation=45)
    plt.legend()
    plt.grid()
    plt.show()

# Exemplo numérico
G = [1, 2, 3, 4]  # Exemplo de grupo
H = [1, 2]        # Subconjunto a ser verificado

if is_subgroup(G, H):
    print(f"H = {H} é um subgrupo de G = {G}.")
else:
    print(f"H = {H} não é um subgrupo de G = {G}.")

# Gerando e visualizando o reticulado de subgrupos
from itertools import combinations

subgroups = subgroup_lattice(G)
visualize_lattice(subgroups)

# Demonstração simbólica usando SymPy
x, y = symbols('x y')
eq1 = Eq(x * y, y * x)  # Comutatividade
eq2 = Eq(x * x.inv(), 1)  # Inverso
display(eq1, eq2)

# Resultados formatados com LaTeX
print("Demonstrações:")
display(eq1)
display(eq2)