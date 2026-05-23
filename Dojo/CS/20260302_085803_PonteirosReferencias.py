# Este código demonstra como uma função pode modificar um objeto passado como argumento em Python. 
# Em Python, listas são mutáveis e, portanto, podem ser alteradas dentro de uma função. 
# O exemplo abaixo mostra uma função que adiciona um elemento a uma lista. 
# Não é necessário instalar bibliotecas adicionais para executar este código.

def adicionar_elemento(lista, elemento):
    lista.append(elemento)

minha_lista = [1, 2, 3]
print("Antes de modificar:", minha_lista)
adicionar_elemento(minha_lista, 4)
print("Depois de modificar:", minha_lista)