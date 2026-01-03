# Este script educacional aborda o conceito de homomorfismos de grupos, incluindo o núcleo, a imagem e isomorfismos. 
# Utilizaremos a biblioteca SymPy para manipulação simbólica, NumPy para computação numérica e Matplotlib para visualizações. 
# O objetivo é demonstrar os conceitos matemáticos de forma prática e visual, facilitando a compreensão.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inicializa a impressão de LaTeX
sp.init_printing()

def homomorfismo_grupo(f, G, H):
    """
    Verifica se uma função é um homomorfismo de grupos.
    
    Parameters:
    f (callable): Função que mapeia elementos de G para H.
    G (list): Conjunto de elementos do grupo G.
    H (list): Conjunto de elementos do grupo H.
    
    Returns:
    bool: True se f é um homomorfismo, False caso contrário.
    """
    for a in G:
        for b in G:
            if f(a * b) != f(a) * f(b):
                return False
    return True

def nucleo(f, G):
    """
    Calcula o núcleo de um homomorfismo de grupo.
    
    Parameters:
    f (callable): Função que mapeia elementos de G para H.
    G (list): Conjunto de elementos do grupo G.
    
    Returns:
    list: Elementos do núcleo.
    """
    return [g for g in G if f(g) == 1]  # 1 é o elemento neutro em H

def imagem(f, G):
    """
    Calcula a imagem de um homomorfismo de grupo.
    
    Parameters:
    f (callable): Função que mapeia elementos de G para H.
    G (list): Conjunto de elementos do grupo G.
    
    Returns:
    set: Elementos da imagem.
    """
    return {f(g) for g in G}

def isomorfismo(f, G, H):
    """
    Verifica se um homomorfismo é um isomorfismo.
    
    Parameters:
    f (callable): Função que mapeia elementos de G para H.
    G (list): Conjunto de elementos do grupo G.
    H (list): Conjunto de elementos do grupo H.
    
    Returns:
    bool: True se f é um isomorfismo, False caso contrário.
    """
    return homomorfismo_grupo(f, G, H) and len(imagem(f, G)) == len(H)

# Exemplo: Homomorfismo do grupo Z_6 para Z_3
G = [0, 1, 2, 3, 4, 5]  # Z_6
H = [0, 1, 2]  # Z_3

def f(x):
    return x % 3  # Mapeia Z_6 para Z_3

# Verificando se f é um homomorfismo
print("f é um homomorfismo:", homomorfismo_grupo(f, G, H))

# Calculando o núcleo e a imagem
nucleo_f = nucleo(f, G)
imagem_f = imagem(f, G)

print("Núcleo de f:", nucleo_f)
print("Imagem de f:", imagem_f)

# Verificando se f é um isomorfismo
print("f é um isomorfismo:", isomorfismo(f, G, H))

# Visualização do núcleo e da imagem
def plot_homomorfismo(G, f):
    """
    Plota a relação entre G e a imagem de f.
    
    Parameters:
    G (list): Conjunto de elementos do grupo G.
    f (callable): Função que mapeia elementos de G para H.
    """
    x = np.array(G)
    y = np.array([f(g) for g in G])
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Imagem de f')
    plt.axhline(0, color='grey', lw=0.5)
    plt.axvline(0, color='grey', lw=0.5)
    plt.title('Homomorfismo de G para H')
    plt.xlabel('Elementos de G')
    plt.ylabel('Elementos de H')
    plt.xticks(G)
    plt.yticks(np.unique(y))
    plt.grid()
    plt.legend()
    plt.show()

plot_homomorfismo(G, f)