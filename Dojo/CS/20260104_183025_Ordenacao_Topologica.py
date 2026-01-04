# Este código implementa a ordenação topológica de um grafo direcionado. 
# A ordenação topológica é usada para resolver problemas de dependência, 
# onde precisamos determinar uma sequência de tarefas a serem executadas, 
# garantindo que cada tarefa seja executada somente após suas dependências. 
# O código utiliza a biblioteca `collections` que já vem com o Python.

from collections import defaultdict, deque

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}  # Inicializa o grau de entrada
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1  # Conta o grau de entrada de cada vértice

    queue = deque([u for u in in_degree if in_degree[u] == 0])  # Vértices sem dependências
    sorted_order = []

    while queue:
        u = queue.popleft()
        sorted_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1  # Remove a dependência
            if in_degree[v] == 0:
                queue.append(v)

    if len(sorted_order) != len(graph):  # Verifica se há ciclo
        return "O grafo contém um ciclo, ordenação não é possível."

    return sorted_order

# Exemplo de uso
grafo = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

resultado = topological_sort(grafo)
print("Ordenação Topológica:", resultado)