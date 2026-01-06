"""
Este script demonstra o conceito de Teste F, que é utilizado para comparar as variâncias de duas populações. 
O teste F é baseado na razão das variâncias amostrais e é frequentemente usado na análise de variância (ANOVA). 
Neste script, utilizaremos SymPy para manipulação simbólica, NumPy para simulações numéricas, 
SciPy para realizar o teste F, e Matplotlib para visualização dos resultados. 
Os dados serão gerados aleatoriamente para simular duas populações com variâncias diferentes.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import sympy as sp

# Inicializa a impressão do SymPy
sp.init_printing()

def calcular_variancia_amostral(dados):
    """
    Calcula a variância amostral de um conjunto de dados.

    :param dados: array-like, conjunto de dados
    :return: variância amostral
    """
    n = len(dados)
    media = np.mean(dados)
    variancia = np.sum((dados - media) ** 2) / (n - 1)
    return variancia

def teste_f(variancia1, variancia2):
    """
    Realiza o teste F para comparar duas variâncias.

    :param variancia1: variância da primeira amostra
    :param variancia2: variância da segunda amostra
    :return: estatística F e valor-p
    """
    F = variancia1 / variancia2
    df1 = len(variancia1) - 1
    df2 = len(variancia2) - 1
    p_value = 1 - stats.f.cdf(F, df1, df2)
    return F, p_value

# Simulação de dados
np.random.seed(42)
n1, n2 = 30, 30
populacao1 = np.random.normal(loc=10, scale=2, size=n1)  # Média 10, desvio padrão 2
populacao2 = np.random.normal(loc=10, scale=5, size=n2)  # Média 10, desvio padrão 5

# Cálculo das variâncias amostrais
variancia1 = calcular_variancia_amostral(populacao1)
variancia2 = calcular_variancia_amostral(populacao2)

# Realizando o teste F
F, p_value = teste_f(variancia1, variancia2)

# Resultados
print(f"Variância amostral 1: {variancia1:.2f}")
print(f"Variância amostral 2: {variancia2:.2f}")
print(f"Estatística F: {F:.2f}")
print(f"Valor-p: {p_value:.4f}")

# Visualização das distribuições
plt.figure(figsize=(12, 6))
plt.hist(populacao1, alpha=0.5, label='População 1 (σ=2)', bins=15)
plt.hist(populacao2, alpha=0.5, label='População 2 (σ=5)', bins=15)
plt.title('Distribuições das Populações')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.legend()
plt.grid()
plt.show()

# Demonstração simbólica do teste F
variancia1_sym, variancia2_sym = sp.symbols('s1 s2')
F_sym = variancia1_sym / variancia2_sym
df1_sym = sp.symbols('df1')
df2_sym = sp.symbols('df2')

# Exibindo a fórmula do teste F
sp.display(sp.Eq(F_sym, variancia1_sym / variancia2_sym))

# Cálculo do valor-p simbólico
valor_p_simbolico = 1 - sp.integrate(stats.f.pdf(F_sym, df1_sym, df2_sym), (F_sym, F_sym, sp.oo))
sp.display(valor_p_simbolico)