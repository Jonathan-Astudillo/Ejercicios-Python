#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
tupla=(2,3,6,7,4,8,9,2,5,6,3,7,3,2)
print("la suma de la tupla es:",sum(tupla))
print("el promedio de la tupla es:",sum(tupla)/len(tupla))
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
tupla_1=(1,3,5,7,8)
tupla_2=(2,4,6,9,2)
suma=0
for e in range(len(tupla_1)):
    suma+= (tupla_1[e]+tupla_2[e])
print("la suma de nuestra funcion es:",suma)
#Crear una tupla de nombres y ordenarla alfabéticamente.
tupla_nom=("Alex","Fabianna","Fernanda","Josue","Kerly")
print(sorted(tupla_nom))
#Crear una tupla de números y encontrar el valor mínimo y máximo.
print("el minimo es.",min(tupla))
print("el valor maximo es:",max(tupla))
#Crear una tupla de números y convertirla en una lista.
lista=list(tupla)
print(type(lista))
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
tupla_semana=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
print("el elemento es:",tupla_semana[3])

#Crear una tupla con números enteros y mostrar aquellos que son pares.
tupla=(2,3,6,7,4,8,9,2,5,6,3,7,3,2)
for e in tupla:
    if e%2 ==0:
        print("los numeros pares son:",e)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
tupla_mes_año=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
for e in tupla_mes_año:
    if len(e)>5:
        print("el mes con mas de 5 letras es:",e)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
tupla_edades=(12,34,25,67,12,11,10,19,18,21,24,23,20,45,23,11)
contar=0
for e in tupla_edades:
    if e >=18:
        contar+=1
print("el total de personas mayores de edad son:",contar)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
tupla_libros= (("pep despues del futbol" ,"albert moren", 2021),
    ("Cien años de soledad", "Gabriel García Márquez", 1967),
    ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
    ("1984", "George Orwell", 1949),
    ("Matar a un ruiseñor", "Harper Lee", 1960))
print(tupla_libros[2][0])