#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
numeros= [1,2,3,4,5]
print("lista de numeros:",numeros)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
nombres= ["Sami","Iker","Fanny","Javier","Carlos"]
print("Primer elemento de la lista es:",nombres[0])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
pares=[1,2,3,4,5,6,7,8,9,10]
for e in pares:
    if e%2 ==0:
        print("los numeros pares son:",e)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
amigos= ["Sami","Iker","Fanny","Javier","Carlos"]
print("Ultimo elemento de la lista es:",amigos[4])

#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
Lista=[1,2,3,4,5,6,7,8,9,10]
print("Ultimo elemento de la lista es:",Lista[-1])

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
impares=[1,2,3,4,5,6,7,8,9,10]
for e in impares:
    if e%2 ==1:
        print("los numeros impares son:",e)
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
nom= ["Sami","Iker","Fanny","Javier","Carlos"]
nom.append("Jonathan")
print("Nombre es:",nom)
#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
muestra=[1,2,3,4,5,6,7,8,9,10]
primer_elemento=muestra[0]
ultimo_elemento=muestra[-1]

print("El primer elemnto es:",primer_elemento)
print("El ultimo elemento es:",ultimo_elemento)

#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
amig= ["Sami","Iker","Fanny","Javier","Carlos"]
print("Total de elementos es:",len(amig))

#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
sum=[1,2,3,4,5,6,7,8,9,10]

operacion= 0

for e in sum:
    operacion += e

print("La suma total es:",operacion)
