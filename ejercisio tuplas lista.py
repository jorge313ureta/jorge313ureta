tupla = (13,1,8,3,2,5,8)
#crear una lista que solo incluya los numeros menore a 5
#e imprima por consola [1,3,2]
lista =[] # definimos fla lista
# filtramos los elemento menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
##