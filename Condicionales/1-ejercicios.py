###CURSO DE FUNDAMENTOS DE PYTHON
##Ejercicios 

#1. Crear una lista de numeros del 1 al 5
num=[1,2,3,4,5]
#2. Accede al elemento 3 de la lista:
num[2]
#3. Modifica un elemento de la lista:
num[3]= 22
#4. Agrega el elemento 9 al final de la lista
num.append(9)
#5. Eliminar el elemento 2 de la lista:
num.remove(2)
#6. Recorrer una lista con un bucle for:
for e in num:
    print(e)
#7. Ordenar una lista:
#num.sort()-->>> otra manera de ver los datos
#print(ventas)
num[::1] #ordenar la lista
num[::-1] #desordenar la lista
#8. Obtener la longitud de una lista:
#print(len(num))->>>otra manera de ver datos 
len(num)
#9. Comprobar si un elemento está en la lista:
5 in num
