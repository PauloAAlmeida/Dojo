# Este código demonstra como uma função pode modificar um objeto passado como argumento em Python. 
# Em Python, listas são mutáveis e podem ser alteradas dentro de funções. 
# O exemplo abaixo mostra uma função que adiciona um elemento a uma lista, 
# demonstrando o conceito de referência.

def adicionar_elemento(lista, elemento):
    lista.append(elemento)

minha_lista = [1, 2, 3]
print("Antes da modificação:", minha_lista)

adicionar_elemento(minha_lista, 4)
print("Depois da modificação:", minha_lista)