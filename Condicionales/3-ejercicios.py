#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla vacía:
tupla_s=()
#Crear una tupla con algunos elementos:
tupla=(10,"hola",[2,4,6,8],["Jonnathan",8])
print(tupla)
#Acceder a un elemento de la tupla:
print(tupla[3])
#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
# Concatenar dos tuplas:
tupla_2=(3,7,9)
tupla=(10,"hola",[2,4,6,8],["Jonnathan",8])
union=tupla+tupla_2
print(union)
#Obtener la longitud de una tupla:
print(len(tupla))
#Convertir una tupla en una lista:
lista= list(tupla)
print(type(lista))
#Convertir una lista en una tupla:
tupla_conv= tuple(lista)
print(type(tupla))