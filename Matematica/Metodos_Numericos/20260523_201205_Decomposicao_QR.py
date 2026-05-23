# O método de decomposição QR é uma técnica fundamental em álgebra linear, utilizada para resolver sistemas de equações lineares, 
# realizar regressão linear e na computação de valores próprios. A decomposição QR de uma matriz A é expressa como A = QR, 
# onde Q é uma matriz ortogonal (ou unitária) e R é uma matriz triangular superior. O método de Gram-Schmidt é um algoritmo 
# que permite obter a matriz Q a partir de um conjunto de vetores linearmente independentes. Neste script, vamos implementar 
# o método de Gram-Schmidt, demonstrar os passos matemáticos com SymPy, e visualizar os resultados com Matplotlib.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializa a impressão em LaTeX
sp.init_printing()

def gram_schmidt(A):
    """
    Realiza a ortogonalização de Gram-Schmidt em uma matriz A.
    
    Parâmetros:
    A (ndarray): Matriz de entrada cujas colunas são vetores a serem ortogonalizados.
    
    Retorna:
    Q (ndarray): Matriz cujas colunas são os vetores ortogonais.
    R (ndarray): Matriz triangular superior.
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    
    return Q, R

# Exemplo numérico
A = np.array([[1, 1, 1], [1, 2, 3], [1, 3, 6]], dtype=float)
Q, R = gram_schmidt(A)

# Resultados
print("Matriz A:")
print(A)
print("\nMatriz Q:")
print(Q)
print("\nMatriz R:")
print(R)

# Visualização dos vetores
def plot_vectors(vectors, colors):
    """
    Plota vetores em um gráfico 2D.
    
    Parâmetros:
    vectors (list): Lista de vetores a serem plotados.
    colors (list): Lista de cores para cada vetor.
    """
    origin = np.zeros((2, len(vectors)))  # Origem dos vetores
    plt.quiver(*origin, vectors[0][:2], vectors[1][:2], angles='xy', scale_units='xy', scale=1, color=colors)
    plt.xlim(-1, 4)
    plt.ylim(-1, 4)
    plt.grid()
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.title('Visualização dos Vetores')
    plt.show()

# Plotando os vetores originais e ortogonais
plot_vectors([A[:, 0], A[:, 1], A[:, 2]], ['r', 'g', 'b'])
plot_vectors([Q[:, 0], Q[:, 1]], ['r', 'g'])

# Demonstração simbólica com SymPy
x1, x2, x3 = sp.symbols('x1 x2 x3')
A_sym = sp.Matrix([[x1, x1, x1], [x1, x2, x3], [x1, x3, x3**2]])
Q_sym, R_sym = sp.qr(A_sym)

# Resultados simbólicos
print("\nDecomposição QR Simbólica:")
sp.pprint(Q_sym)
sp.pprint(R_sym)

# Exemplo com dados simulados para regressão linear
np.random.seed(0)
x_data = np.random.rand(10, 1) * 10
y_data = 2.5 * x_data + np.random.randn(10, 1) * 2

# Montando a matriz A com um termo constante
A_reg = np.hstack((np.ones((x_data.shape[0], 1)), x_data))
Q_reg, R_reg = gram_schmidt(A_reg)

# Coeficientes da regressão
beta = np.linalg.solve(R_reg, Q_reg.T @ y_data)

print("\nCoeficientes da Regressão Linear:")
print(beta)