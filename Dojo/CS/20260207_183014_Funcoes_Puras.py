# Este código demonstra o conceito de funções puras em Python. Uma função pura é aquela que, para um dado conjunto de entradas, sempre produz a mesma saída e não causa efeitos colaterais (não altera variáveis externas, não imprime nada, etc.). Neste exemplo, criaremos uma função que calcula o quadrado de um número. 
# Para executar este código, não são necessárias bibliotecas externas.

def quadrado(x):
    return x * x

resultado = quadrado(5)
print("O quadrado de 5 é:", resultado)