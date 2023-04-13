#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#Crear un diccionario vacío:
diccionario={}
#Agregar elementos a un diccionario:
diccionario["llave 1"]=10
diccionario["llave 2"]=23
diccionario["llave 3"]=45
diccionario["llave 4"]=65
print(diccionario)
#Acceder a un valor en un diccionario:
print(diccionario["llave 3"])
#Verificar si una llave existe en un diccionario:
print(diccionario.keys())
#Eliminar un elemento de un diccionario:
print(diccionario.pop("llave 4"))
#Imprimir las llaves de un diccionario:
print(diccionario.keys())
#Imprimir los valores de un diccionario:
print(diccionario.values())
#Imprimir las llaves y valores de un diccionario:
print(diccionario.items())
