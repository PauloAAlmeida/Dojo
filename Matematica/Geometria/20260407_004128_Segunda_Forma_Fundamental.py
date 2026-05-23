"""
Este script explora a Segunda Forma Fundamental da geometria diferencial, que descreve a curvatura das superfícies. 
A Segunda Forma Fundamental é uma matriz que captura a curvatura de uma superfície em um ponto, permitindo a análise de 
como a superfície se curva em relação ao espaço tridimensional. Usaremos a biblioteca SymPy para manipulação simbólica, 
NumPy para cálculos numéricos e Matplotlib para visualizações gráficas.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Inicializa a impressão em LaTeX
sp.init_printing()

def segunda_forma_fundamental(superficie, u, v):
    """
    Calcula a Segunda Forma Fundamental de uma superfície dada em coordenadas paramétricas.

    Parameters:
    superficie (list): Lista de funções que definem a superfície em termos de u e v.
    u (symbol): Variável paramétrica u.
    v (symbol): Variável paramétrica v.

    Returns:
    F (Matrix): Segunda Forma Fundamental da superfície.
    """
    # Derivadas parciais
    r_u = [sp.diff(f, u) for f in superficie]
    r_v = [sp.diff(f, v) for f in superficie]
    
    # Vetor normal
    normal = sp.Matrix(r_u).cross(sp.Matrix(r_v))
    normal = normal / normal.norm()  # Normaliza o vetor normal
    
    # Segunda Forma Fundamental
    F = []
    for i in range(len(superficie)):
        F.append(sp.diff(normal, u).dot(sp.Matrix(r_u)) + sp.diff(normal, v).dot(sp.Matrix(r_v)))
    
    return sp.Matrix(F)

# Definindo a superfície como uma parábola
u, v = sp.symbols('u v')
superficie = [u, v, u**2 + v**2]

# Calculando a Segunda Forma Fundamental
F = segunda_forma_fundamental(superficie, u, v)
sp.display(F)

# Função para visualizar a superfície
def plot_superficie(superficie_func, u_range, v_range):
    """
    Plota uma superfície definida por uma função em um espaço tridimensional.

    Parameters:
    superficie_func (function): Função que define a superfície.
    u_range (tuple): Intervalo para u (min, max).
    v_range (tuple): Intervalo para v (min, max).
    """
    u_vals = np.linspace(u_range[0], u_range[1], 100)
    v_vals = np.linspace(v_range[0], v_range[1], 100)
    U, V = np.meshgrid(u_vals, v_vals)
    
    # Avaliando a superfície
    X = U
    Y = V
    Z = U**2 + V**2
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='cyan')
    
    # Adicionando detalhes
    ax.set_xlabel('U')
    ax.set_ylabel('V')
    ax.set_zlabel('Z')
    ax.set_title('Superfície: Z = U^2 + V^2')
    plt.show()

# Visualizando a superfície
plot_superficie(superficie, (-2, 2), (-2, 2))

# Exemplo numérico da Segunda Forma Fundamental
def exemplo_numerico():
    """
    Executa um exemplo numérico da Segunda Forma Fundamental em um ponto específico da superfície.
    """
    # Definindo um ponto na superfície
    u_val = 1
    v_val = 1
    F_num = F.subs({u: u_val, v: v_val})
    print(f"Segunda Forma Fundamental no ponto (u={u_val}, v={v_val}):")
    sp.pprint(F_num)

# Executando o exemplo numérico
exemplo_numerico()