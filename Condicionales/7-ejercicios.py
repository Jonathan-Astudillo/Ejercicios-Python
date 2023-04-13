#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
numeros= set(range(1,11))
print(numeros)
#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.
num_par=set(range(2,11,2))
print("numeros pares:",num_par)
num_impar=set(range(1,11,2))
print("numeros impares",num_impar)
#interseccion
inter=num_par&num_impar
print("los valores intersectados son:",inter)
#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas={"manzana", "banana" "naranja"}
dato=input("introduce la fruta")
if dato in frutas:
    print("la fruta",dato,"esta en el conjunto")
else:
    print("la fruta",dato,"no esta en el conjunto")
#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
# Crear conjuntos
conjunto1 = set(range(1, 6))
conjunto2 = set(range(4, 9))

# Unir los conjuntos
union_conjunto= conjunto1.union(conjunto2)

# Eliminar los elementos repetidos
conjunto_sin_repetidos = set()
for elemento in union_conjunto:
    if elemento not in conjunto_sin_repetidos:
        conjunto_sin_repetidos.add(elemento)

# Imprimir el conjunto resultante
print(conjunto_sin_repetidos)

#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.

# Crear conjuntos
conjunto1 = set(range(1, 6))
conjunto2 = set(range(4, 9))

# Unir los conjuntos
conjunto_unido = conjunto1.union(conjunto2)

# Eliminar los elementos repetidos
conjunto_sin_repetidos = set()
for elemento in conjunto_unido:
    if elemento not in conjunto_sin_repetidos:
        conjunto_sin_repetidos.add(elemento)

# Imprimir el conjunto resultante
print(conjunto_sin_repetidos)


#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.

# Crear conjunto
compras = {"leche", "pan", "huevos", "azúcar"}

# Eliminar elemento "azúcar" del conjunto
compras.remove("azúcar")

# Agregar elemento "harina" al conjunto
compras.add("harina")

# Imprimir conjunto resultante
print(compras)


#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.

# Crear conjunto
nombres = {"Juan", "María", "Pedro", "Luisa"}

# Imprimir número de elementos del conjunto
print(len(nombres))


#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.

# Crear conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimir conjuntos
print("conjunto1:", conjunto1)
print("conjunto2:", conjunto2)

# Imprimir diferencia simétrica
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("diferencia simétrica:", diferencia_simetrica)


#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.

# Crear conjuntos
conjunto1 = set(range(1, 11))
conjunto2 = set(range(5, 16))

# Imprimir conjuntos
print("conjunto1:", conjunto1)
print("conjunto2:", conjunto2)

# Imprimir unión
union = conjunto1.union(conjunto2)
print("unión:", union)


#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.

# Crear conjunto
frutas = {"manzana", "banana", "naranja", "pera"}

# Imprimir elementos en orden alfabético
print(sorted(frutas))


#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.

# Crear conjuntos
conjunto1 = set(range(1, 11))
conjunto2 = set(range(6, 16))

# Imprimir conjuntos
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Calcular intersección
interseccion = conjunto1.intersection(conjunto2)

# Imprimir intersección
print("Intersección:", interseccion)