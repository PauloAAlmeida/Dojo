import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import minimize
from sympy import init_printing

# Inicializa a impressão do SymPy para formato LaTeX
init_printing()

# Definindo a função e suas derivadas
def define_function():
    x = sp.symbols('x')
    f = x**4 - 3*x**3 + 2  # Função a ser otimizada
    f_prime = sp.diff(f, x)  # Derivada primeira
    f_double_prime = sp.diff(f_prime, x)  # Derivada segunda
    return f, f_prime, f_double_prime

# Método de Newton para otimização
def newton_method(f_prime, f_double_prime, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        f_prime_val = f_prime.subs('x', x).evalf()
        f_double_prime_val = f_double_prime.subs('x', x).evalf()
        if f_double_prime_val == 0:
            raise ValueError("Hessiana é zero, não é possível continuar.")
        x_new = x - f_prime_val / f_double_prime_val
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

# Visualização da função e do ponto ótimo
def plot_function(f, x_opt):
    x_vals = np.linspace(-1, 3, 400)
    y_vals = [f.evalf(subs={'x': val}) for val in x_vals]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.scatter([x_opt], [f.evalf(subs={'x': x_opt})], color='red', zorder=5)
    plt.title('Otimização usando o Método de Newton')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()

# Função principal
def main():
    f, f_prime, f_double_prime = define_function()
    x0 = 0.5  # Chute inicial
    x_opt, iterations = newton_method(f_prime, f_double_prime, x0)
    
    print(f"Solução encontrada: x = {x_opt:.4f} em {iterations} iterações.")
    print("Valor da função no ponto ótimo:", f.evalf(subs={'x': x_opt}))
    
    plot_function(f, x_opt)

if __name__ == "__main__":
    main()