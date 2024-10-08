##lista =ariel ,liliana,natalia,osvaldo
nombres = ["Naty","Osvaldo","Lily","Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])###recuperar solo muestr el indice 0,1 pero no el indice 2
#ir del indice  de la lista al indice ({sin incluir)})
print(nombres[ :3])#desde el indice hastael final
print(nombres[1: ])#mo
#modificar un valor
nombres[3] = "liliana"
print(nombres)
nombres[2] = "natalia"
nombres[0] = "ariel"
print(nombres)
#iterar una lista
for nombres in nombres: #nombre es singular ,la lista es plural
    print(nombres)
else:
    print("se acabaron los elementos de la listas")   
     #preguntamos cuantos elementos de la lista
print(len(nombres)) #le pasamos como parametros la lista
#agregamos un elemento
nombres.append(Marcelo)
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)
#insertar un elemento en un indice espacifico
nombres.insert(1,"albert")
print(nombres)
nombres.insert(3,"debora") 
print(nombres)   
 #eliminar un elemento 
nombres.remove("albert") 
print(nombres)#             
#ieliminar el ultimo elemento
nombres.pop()
#ELIMINAR UN INDICE ESPESIFICO
del nombres[2]#del significar delete (eliminar)
print(nombres)
#eliminar borrar o limpiar todos los elementos
nombres.clear(nombres)
print(nombres)
#para elininar lista
del nombres
print(nombres)
#ejercisio 3 crear un rango de 3 10 pero con incremento de 2 en 2 , en lugar de 1 en 1 
#ejemplo de ejecucion :0,3,6,9
print("rango de 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)
 #ejercisio 2 : crear un rango de numeros de 2 a 6 a imprielo
 # "ejemplo de ejercucion : 2,3,4,5,6
print("rango con valores de inicio = 2 y fin = 6")
rango = range (2,7)
for i in rango:
    print(i)
#ejercisio 3 : crear un rango de 3 a 10 pero con incremento de 2 en 2 ,en lugar de 1 en 1
# #ejercisio de ejecucion : 3,4,6,7,9
print("rango con valores de inicio = 3,fin  = 10,incremento = 2")    
for i  in range(3,11,2):
    print(i)
#trabajar     
#definirmos una tupla
cocina = ("cuchara", "cuchillo","tenedor")
print(len(cocina))
#acceder a un elemento,para esto utilizamos corchetes no parantesis
print(cocina[o])
#mostrar manera inversa
print(cocina[-1])
#como acceder a un rango
print(cocina[0:1])
print(cocina[0:2])
#ejemplo
verdura = ("papa")#una tupla necesita aunque sea de un elemento: la coma
# de lo contrario seria un tipo str cadena
#recorrer los elemtos de la tupla
for cocinar in cocina:
    print(cocinar , end = " ")# print esta usando /n para saltos de linea
# usamos end= para eliminar los saltos de lineas
cocina[0] = "plato"
print(cocina)# muetra un error no se puede agregar un hacer una modificacion en la tupla
#para modificar tupla a lista
cocinalista = list(cocina)
cocinalista [0] = "plato"
cocina = tuple(cocinalista)
print("\n" ,cocina )
del  cocina
print(cocina)#eliminar la tupla
#tipo set
planetas = {"marte","jupiter","venus"}
print(len(planetas))# usamos la funcion len= length significa largo
#revisar si un elemento existe dentro de set
print("marte"in planetas)# poner los elementos identico "false" o true si se coloca bien
#agregar elementos
planetas.add("tierra")#add es una funcion
print(planetas)
#los duplicados no se puedes aplicados o rrepetidos
#eliminar elementos,puede arrojar un error si el elemento no existe
planetas.remove("jupite")# si nos olvidamos algo   error
print(planetas)
# borra el elemento
planetas.discard("tierra")
print(planetas)#con discard repara el error diferencia no presenta error
#limpiar set
planetas.clear()
print(planetas)#limpiar set
# eliminar set
del planetas
#print(planetas)# presenta error

# "maradona" : 10  es un dicciionario esta compuesto por dos elementos 
# una llave y un valor
#dict (key,value)
diccionario ={
    "IDE" : "Integrated Development","poo" :"programacion orientada a objetos", "SABD": "sISTEMA DE aDMINISTRACION DE ase de datos",
}
print(len(diccionario))
print(diccionario["IDE"])

#accede a un dicionario con la llave {8key}
print(diccionario.get("POO"))
print(diccionario.get("SABD"))
#MODIFICAR LOS ELEMENTOS
diccionario["IDE"]= "ENTORNO DE DESARROLLO INTEGRADO"
print(diccionario)
#DICCIONARIO PARTE DOS COMO RECORRER LOS ELEMENTOS CON BUCLE FOR
for termino  in diccionario:
    print(termino)
for termino, valor  in diccionario. items():# recorrer mostrar solo las llaves
    print(termino,valor)    

#otras maneras de acceder a un diccionario
for termino in diccionario.items():
    print(termino) # muestra solo las llaves
for valor in diccionario.values():#usamos una funcion para acceder al valor
    print(valor)    

#comprobar la existencia de algun elemento
print("IDE" in diccionario)# devuelve un booleano
#agrgar un elemento 
diccionario["PK"]= "primary key"
print(diccionario)
#eliminar un elemento
diccionario.pop("SABD")
print(diccionario)
#vaciar un diccionario 
diccionario.clear()
print(diccionario)
#elimnar diccionario
del diccionario#el diccionario se borro
print(diccionario)
#cocadtenamos listas 
# ecciones en python #las listas es lo que se conoce en otros lenguajes como arreglos o vectores
lista1 =[1,2,3]# aqui agregamos otro numero 1
lista2 =[4,5,6]# aqui tambien  count dice cuantos mas hay 4 mas 1
lista3 = lista1 + lista2 #concatenacion
print(lista3)
lista3.extend([7,8,9])#funcion para agregar varios elementos a una lista
print(lista3)
print(lista3.index(5))# funcion para ubicar en que indice esta el valor ingresado
print(lista3.index(0))#esto daria un error por no ser el elementos parte de la lista
#como saber cuantos valores repetidos hay dentro deuna lista 
print(lista3.count(1))#cuanta ccuantos valore iguales hay dentro de una lista

#par poner al reves una lista 
lista3.reverse()
print(lista3)
#para que una lista se multiplique repitiendo susu elementos
lista = [1,2,3] *2#lista3 = lista3 *2 sea repetido
print(lista3)
#metodos de aordenamientos
lista3.sort()# orednar asendentemente 
print(lista3)
lista3.sort(reverse = True)#ordenar desendente
print(lista3)
#tuplas 
tupla = (4,"Hola", 6,78,[1,2,78],4, "Hola")
print(tupla)#puede tener diferentes tipos de datos dentro
print(4 in tupla)#accion  booleana ,su rrspeta es de tipo booleana
#lo que podemos usar de ntro de tuplas son : index , count, len,
#en tuplas se puede converir de tuplas a listas y de listas a tuplas

#repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye",}#con las llavessola no se puede comenzar,con el set 
conjunto2 .add(7)
conjunto2.add("Hola")
print(conjunto2)
#conjunto1.add(9)#7,8 no se le puede añadir nada
conjunto1.add("bye")
print(conjunto1)
print(3 not in conjunto1)#preguntamos si el numero 3 no esta en el conjunto1
#noes devuelve un valor booleano en la consola
#como hacer la igualdad de dos conjuntos
print(conjunto1 ==conjunto2)#nos devuelve como respuesta un booleano
#operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2#la linea une los  dos conjuntos
print(conjunto3)
#no debe haber igualdad si no borra uno
#la interseccion
conjunto3 = conjunto1 & conjunto2 #que elementos tienen en comun
print(conjunto3)
conjunto3 = conjunto1 - conjunto2#asigna el valor que esta en el conjunto1 y no en el conjunto2

print(conjunto3)
conjunto3 = conjunto2 - conjunto1 #
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2 # son los elementos que estan en los 2 conjuntos y no estan compartidos
print(conjunto3)
#
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))#aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))
print(conjunto3.issuperset(conjunto1))#preguntamos silos elementos del conjunto1es estan dentro del 3

print(conjunto3.issuperset(conjunto2))# si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos  ,estos es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))#no hay cosas en comun al cambiar hola que no hay
#convertir un cojunto otalmente en inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente inmutable
#no se puede agregar ,modificar ni eliminar elementos del conjunto
#repaso diccionario
diccionarioNuevo = {"azul":"blue","rojo": "red", "verde":"green","amarillo":"yellow"}
#como eliminar
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)
#los didciccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"ariel":{"edad": 40, "altura":1.83},"osvaldo":[45,1.85],"natalia":[35,1.67]}
print(diccionario2)
seleccionArgentina ={
    10: {"nombre": "lionel messi","edad":35, "altura":1.70,"precio":"50 millones","posicion":"extremo derecho"},
    11: {"nombre": "angel di maria","edad":34,"altura":1.80,"precio":"11 millones","posiscion":"extremo derecho"},
    24: {"nombre": "paulo dybala","edad":28,"altura":1.77,"precio":"12 millones","posision":"media punta"},
    19: {"nombre": "nicolas otamendi","edad":34,"altura":1.83,"precio":"3,5 millones","posicion":"defensa central"},
    1:  {"nombre": "franco armani","edad":35,"altura":1.89,"precio":"3.5 millones","posicion":"portero"},
    9: {"nombre": "julian alvares","edad":24,"altura":1.70,"precio":"90 millones","posicion":"delantero"},
    22:{"nombre": "lautaro martinez","edad":27,"altura":1.75,"precio":"75 millones","posicion":"delantero"},
    5: {"nombre": "leandro paredes","edad":30,"altura": 1.80,"precio":"30 millones","posicion": "mediocampista"},
    4: {"nombre": "gonzalo montiel","edad":27,"altura": 1.75,"precio":"12 millones","posicion": "defensor"},
}
for llave, valor in seleccionArgentina.items():
    print(llave,valor)
    #como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print(len(seleccionArgentina))
#pilas usando listas 
pila = [1,2,3]
#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)
#sacando elementos desde el final
pila.pop()
print(pila)
elementoBorrado = pila.pop()#quita el ultimo elemento y lo guarda en la variable.
print(f"sacamos  elelemento: [elemetoBorrado]")
print(f"la pila ahora quedo asi:{pila}")
#colas con listas
#estructura de datos de tipo fifo (fitst input /first output)
cola = ["ariel","osvaldo","liliana","pilar"]
#agregamos elementos al final de la cola
cola.append("natalia")
cola.append("jose")
print(cola)
#sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido{seRetira}")
print(cola)
##
