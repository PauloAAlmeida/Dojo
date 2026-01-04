# A Análise Discriminante é uma técnica estatística utilizada para classificar observações em diferentes grupos. 
# Existem duas abordagens principais: Análise Discriminante Linear (LDA) e Análise Discriminante Quadrática (QDA). 
# A LDA assume que as classes compartilham a mesma matriz de covariância, enquanto a QDA permite que cada classe tenha sua própria matriz de covariância. 
# Neste script, vamos demonstrar ambos os métodos usando Python, incluindo a teoria por trás deles e exemplos práticos com visualizações.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from sympy import symbols, Matrix, init_printing, simplify

init_printing()

# Função para calcular a matriz de covariância
def covariance_matrix(data):
    """
    Calcula a matriz de covariância de um conjunto de dados.
    
    Parameters:
    data (np.ndarray): Conjunto de dados onde cada linha é uma observação e cada coluna é uma variável.
    
    Returns:
    np.ndarray: Matriz de covariância.
    """
    return np.cov(data, rowvar=False)

# Função para calcular a média
def mean_vector(data):
    """
    Calcula o vetor de médias de um conjunto de dados.
    
    Parameters:
    data (np.ndarray): Conjunto de dados onde cada linha é uma observação e cada coluna é uma variável.
    
    Returns:
    np.ndarray: Vetor de médias.
    """
    return np.mean(data, axis=0)

# Função para LDA
def lda_fit(X, y):
    """
    Ajusta um modelo LDA aos dados.
    
    Parameters:
    X (np.ndarray): Conjunto de dados.
    y (np.ndarray): Rótulos das classes.
    
    Returns:
    dict: Coeficientes do modelo LDA.
    """
    classes = np.unique(y)
    means = {}
    cov = np.zeros((X.shape[1], X.shape[1]))
    
    for cls in classes:
        X_cls = X[y == cls]
        means[cls] = mean_vector(X_cls)
        cov += covariance_matrix(X_cls) * (len(X_cls) - 1)
    
    cov /= (len(X) - len(classes))
    return {'means': means, 'cov': cov}

# Função para prever usando LDA
def lda_predict(model, X):
    """
    Faz previsões usando o modelo LDA.
    
    Parameters:
    model (dict): Modelo LDA ajustado.
    X (np.ndarray): Conjunto de dados para prever.
    
    Returns:
    np.ndarray: Rótulos previstos.
    """
    means = model['means']
    cov = model['cov']
    inv_cov = np.linalg.inv(cov)
    priors = {cls: len(X[y == cls]) / len(X) for cls in means.keys()}
    
    scores = {}
    for cls, mean in means.items():
        score = (X @ inv_cov @ mean) - (0.5 * mean.T @ inv_cov @ mean) + np.log(priors[cls])
        scores[cls] = score
    
    return np.argmax(np.array(list(scores.values())), axis=0)

# Função para QDA
def qda_fit(X, y):
    """
    Ajusta um modelo QDA aos dados.
    
    Parameters:
    X (np.ndarray): Conjunto de dados.
    y (np.ndarray): Rótulos das classes.
    
    Returns:
    dict: Coeficientes do modelo QDA.
    """
    classes = np.unique(y)
    means = {}
    covs = {}
    
    for cls in classes:
        X_cls = X[y == cls]
        means[cls] = mean_vector(X_cls)
        covs[cls] = covariance_matrix(X_cls)
    
    return {'means': means, 'covs': covs}

# Função para prever usando QDA
def qda_predict(model, X):
    """
    Faz previsões usando o modelo QDA.
    
    Parameters:
    model (dict): Modelo QDA ajustado.
    X (np.ndarray): Conjunto de dados para prever.
    
    Returns:
    np.ndarray: Rótulos previstos.
    """
    means = model['means']
    covs = model['covs']
    priors = {cls: len(X[y == cls]) / len(X) for cls in means.keys()}
    
    scores = {}
    for cls, mean in means.items():
        inv_cov = np.linalg.inv(covs[cls])
        score = (-0.5 * (X - mean) @ inv_cov @ (X - mean).T).diagonal() + np.log(priors[cls])
        scores[cls] = score
    
    return np.argmax(np.array(list(scores.values())), axis=0)

# Gerando dados simulados
np.random.seed(0)
n_samples = 100
X1 = np.random.normal(loc=0, scale=1, size=(n_samples, 2))
X2 = np.random.normal(loc=3, scale=1, size=(n_samples, 2))
X = np.vstack((X1, X2))
y = np.array([0] * n_samples + [1] * n_samples)

# Ajustando e prevendo com LDA
lda_model = lda_fit(X, y)
lda_predictions = lda_predict(lda_model, X)

# Ajustando e prevendo com QDA
qda_model = qda_fit(X, y)
qda_predictions = qda_predict(qda_model, X)

# Visualizando os resultados
plt.figure(figsize=(12, 6))

# LDA
plt.subplot(1, 2, 1)
plt.title("LDA")
plt.scatter(X[:, 0], X[:, 1], c=lda_predictions, cmap='coolwarm', alpha=0.5)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# QDA
plt.subplot(1, 2, 2)
plt.title("QDA")
plt.scatter(X[:, 0], X[:, 1], c=qda_predictions, cmap='coolwarm', alpha=0.5)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.tight_layout()
plt.show()