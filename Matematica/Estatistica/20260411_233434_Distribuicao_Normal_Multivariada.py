# A distribuição normal multivariada é uma generalização da distribuição normal univariada para múltiplas variáveis. 
# Ela é caracterizada por um vetor de médias e uma matriz de covariância. 
# As propriedades dessa distribuição incluem a simetria em torno da média e a forma elipsoidal da densidade de probabilidade. 
# Neste script, vamos explorar suas propriedades, realizar simulações e visualizar os resultados.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal
import sympy as sp

# Inicializa a impressão do SymPy
sp.init_printing()

def calcular_densidade_multivariada(media, cov, x):
    """
    Calcula a densidade de probabilidade da distribuição normal multivariada.
    
    :param media: vetor de médias
    :param cov: matriz de covariância
    :param x: ponto onde calcular a densidade
    :return: densidade de probabilidade
    """
    return multivariate_normal.pdf(x, mean=media, cov=cov)

def visualizar_densidade_2d(media, cov):
    """
    Visualiza a densidade de probabilidade da distribuição normal multivariada em 2D.
    
    :param media: vetor de médias
    :param cov: matriz de covariância
    """
    x = np.linspace(media[0] - 3 * np.sqrt(cov[0, 0]), media[0] + 3 * np.sqrt(cov[0, 0]), 100)
    y = np.linspace(media[1] - 3 * np.sqrt(cov[1, 1]), media[1] + 3 * np.sqrt(cov[1, 1]), 100)
    X, Y = np.meshgrid(x, y)
    
    pos = np.dstack((X, Y))
    Z = multivariate_normal.pdf(pos, mean=media, cov=cov)
    
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.scatter(media[0], media[1], color='red', marker='x', s=100)
    plt.title('Densidade da Distribuição Normal Multivariada')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.show()

def demonstrar_propriedades(cov):
    """
    Demonstra as propriedades da matriz de covariância e a relação com a forma da distribuição.
    
    :param cov: matriz de covariância
    """
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    print("Valores próprios (variâncias):", eigenvalues)
    print("Vetores próprios (direções):", eigenvectors)

    # Visualização dos eixos principais
    plt.quiver(0, 0, eigenvectors[0, 0], eigenvectors[1, 0], 
               angles='xy', scale_units='xy', scale=1, color='r', label='Eixo 1')
    plt.quiver(0, 0, eigenvectors[0, 1], eigenvectors[1, 1], 
               angles='xy', scale_units='xy', scale=1, color='b', label='Eixo 2')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.title('Eixos principais da matriz de covariância')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# Definindo a média e a matriz de covariância
media = np.array([0, 0])
cov = np.array([[1, 0.8], [0.8, 1]])

# Visualizando a densidade
visualizar_densidade_2d(media, cov)

# Demonstrando propriedades
demonstrar_propriedades(cov)

# Simulação de dados
np.random.seed(42)
dados = np.random.multivariate_normal(media, cov, 500)

# Visualizando os dados simulados
sns.scatterplot(x=dados[:, 0], y=dados[:, 1], alpha=0.5)
plt.title('Dados Simulados da Distribuição Normal Multivariada')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.axis('equal')
plt.show()