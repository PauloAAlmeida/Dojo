# Este script explora as hipérboles, suas assíntotas, focos e aplicações. 
# A hipérbole é uma das cônicas e é definida como o conjunto de pontos cuja diferença das distâncias a dois pontos fixos (focos) é constante. 
# Vamos usar o SymPy para manipulação simbólica, NumPy para computação numérica e Matplotlib para visualização.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializa a impressão do SymPy
sp.init_printing()

def hiperbole(a, b):
    """
    Gera a equação da hipérbole e suas propriedades.
    
    Parâmetros:
    a (float): Distância do centro até os vértices na direção x.
    b (float): Distância do centro até os vértices na direção y.
    
    Retorna:
    eq (sympy.Eq): Equação da hipérbole.
    focos (tuple): Coordenadas dos focos da hipérbole.
    assintotas (list): Equações das assíntotas.
    """
    x, y = sp.symbols('x y')
    c = sp.sqrt(a**2 + b**2)
    
    # Equação da hipérbole
    eq = sp.Eq((x**2 / a**2) - (y**2 / b**2), 1)
    
    # Focos
    focos = (c, 0), (-c, 0)
    
    # Assintotas
    assintota1 = sp.Eq(y, (b/a) * x)
    assintota2 = sp.Eq(y, -(b/a) * x)
    
    return eq, focos, [assintota1, assintota2]

# Definindo parâmetros da hipérbole
a = 3
b = 2
eq, focos, assintotas = hiperbole(a, b)

# Exibindo resultados
print("Equação da hipérbole:")
sp.pprint(eq)

print("\nFocos da hipérbole:")
print(f"Foco 1: {focos[0]}, Foco 2: {focos[1]}")

print("\nAssintotas:")
for assintota in assintotas:
    sp.pprint(assintota)

def plot_hiperbole(a, b):
    """
    Plota a hipérbole e suas assintotas.
    
    Parâmetros:
    a (float): Distância do centro até os vértices na direção x.
    b (float): Distância do centro até os vértices na direção y.
    """
    x = np.linspace(-10, 10, 400)
    y1 = (b/a) * np.sqrt((x**2/a**2) - 1)
    y2 = -(b/a) * np.sqrt((x**2/a**2) - 1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='Hipérbole', color='blue')
    plt.plot(x, y2, color='blue')
    
    # Assintotas
    plt.plot(x, (b/a) * x, 'r--', label='Assintota 1')
    plt.plot(x, -(b/a) * x, 'r--', label='Assintota 2')
    
    # Focos
    plt.scatter([focos[0][0], focos[1][0]], [focos[0][1], focos[1][1]], color='black', label='Focos')
    
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.title('Hipérbole e suas Assintotas')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.axis('equal')
    plt.show()

# Plotando a hipérbole
plot_hiperbole(a, b)

# Exemplo de aplicação: simulação de dados
def simular_dados(n=100, a=3, b=2):
    """
    Simula dados que seguem a forma de uma hipérbole.
    
    Parâmetros:
    n (int): Número de pontos a serem gerados.
    a (float): Distância do centro até os vértices na direção x.
    b (float): Distância do centro até os vértices na direção y.
    
    Retorna:
    dados (numpy.ndarray): Array de dados simulados.
    """
    x = np.linspace(-10, 10, n)
    y = (b/a) * np.sqrt((x**2/a**2) - 1)
    dados = np.column_stack((x, y))
    return dados

# Gerando dados simulados
dados = simular_dados()

# Visualizando os dados simulados
plt.scatter(dados[:, 0], dados[:, 1], color='green', label='Dados Simulados')
plt.title('Dados Simulados em Forma de Hipérbole')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.axis('equal')
plt.show()