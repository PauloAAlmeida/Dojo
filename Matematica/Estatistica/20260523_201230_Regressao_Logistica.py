# A Regressão Logística é um modelo estatístico que é usado para prever a probabilidade de um evento binário, 
# como sucesso ou fracasso. O modelo é baseado na função logística, que transforma a combinação linear das variáveis 
# independentes em uma probabilidade entre 0 e 1. O Odds Ratio é uma medida que compara as chances de um evento ocorrer 
# em dois grupos diferentes. A curva ROC (Receiver Operating Characteristic) é uma ferramenta gráfica que ilustra 
# a capacidade de um modelo de classificar corretamente os eventos. Neste script, vamos explorar esses conceitos 
# usando Python e suas bibliotecas.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

# Inicializa a impressão do SymPy
sp.init_printing()

def odds_ratio(a, b, c, d):
    """
    Calcula o Odds Ratio a partir de uma tabela de contingência.
    
    Parameters:
    a (int): Número de eventos no grupo 1
    b (int): Número de não eventos no grupo 1
    c (int): Número de eventos no grupo 2
    d (int): Número de não eventos no grupo 2
    
    Returns:
    float: Odds Ratio
    """
    return (a / b) / (c / d)

def logistic_function(x):
    """
    Calcula a função logística.
    
    Parameters:
    x (float): Valor de entrada
    
    Returns:
    float: Valor da função logística
    """
    return 1 / (1 + np.exp(-x))

def plot_logistic_curve():
    """
    Plota a curva da função logística.
    """
    x = np.linspace(-10, 10, 100)
    y = logistic_function(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Função Logística', color='blue')
    plt.title('Curva da Função Logística')
    plt.xlabel('x')
    plt.ylabel('P(y=1)')
    plt.axhline(0.5, color='red', linestyle='--')
    plt.axvline(0, color='green', linestyle='--')
    plt.legend()
    plt.grid()
    plt.show()

def simulate_data(n=100):
    """
    Simula dados binários para a regressão logística.
    
    Parameters:
    n (int): Número de observações
    
    Returns:
    tuple: Variáveis independentes (X) e dependentes (y)
    """
    np.random.seed(0)
    X = np.random.normal(0, 1, n)
    y = np.random.binomial(1, logistic_function(X))
    return X.reshape(-1, 1), y

def fit_logistic_regression(X, y):
    """
    Ajusta um modelo de regressão logística aos dados.
    
    Parameters:
    X (array): Variáveis independentes
    y (array): Variável dependente
    
    Returns:
    LogisticRegression: Modelo ajustado
    """
    model = LogisticRegression()
    model.fit(X, y)
    return model

def plot_roc_curve(model, X, y):
    """
    Plota a curva ROC para o modelo de regressão logística.
    
    Parameters:
    model (LogisticRegression): Modelo ajustado
    X (array): Variáveis independentes
    y (array): Variável dependente
    """
    y_scores = model.predict_proba(X)[:, 1]
    fpr, tpr, _ = roc_curve(y, y_scores)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(10, 6))
    plt.plot(fpr, tpr, color='blue', label='Curva ROC (Área = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='red', linestyle='--')
    plt.title('Curva ROC')
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.legend()
    plt.grid()
    plt.show()

# Demonstração do cálculo do Odds Ratio
a, b, c, d = 20, 30, 15, 35
or_value = odds_ratio(a, b, c, d)
print(f'Odds Ratio: {or_value:.2f}')

# Demonstração da função logística
plot_logistic_curve()

# Simulação de dados e ajuste do modelo
X, y = simulate_data(n=100)
model = fit_logistic_regression(X, y)

# Plot da curva ROC
plot_roc_curve(model, X, y)