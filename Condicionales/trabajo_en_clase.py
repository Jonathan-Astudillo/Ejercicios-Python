#1. Crear una lista de numeros del 1 al 5
ventas=[10,20,30,40,50,60,70,80]
#2. Accede al elemento 3 de la lista:
print(ventas[2])
#3. Modifica un elemento de la lista:
ventas[3]= [100]
print(ventas)
#4. Agrega el elemento 9 al final de la lista
ventas.append(120)
#5. Eliminar el elemento 2 de la lista:
ventas.remove(20)
print(ventas)
#6. Recorrer una lista con un bucle for:
for e in ventas:
    print(e)
#7. Ordenar una lista:
#ventas.sort()
print(ventas)

#ventas.sort(reverse=True)

#8. Obtener la longitud de una lista:
print(len(ventas)) 

#9. Comprobar si un elemento está en la lista:
if 120 in ventas:
    print("El numero esta dentro de la lista:")
else:
    print("El numero no esta en la lista")