# Este código calcula o fatorial de um número usando recursão. 
# O fatorial de um número n (denotado como n!) é o produto de todos os números inteiros positivos até n. 
# Por exemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120. 
# A função recursiva chama a si mesma até atingir o caso base, que é 1. 

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")