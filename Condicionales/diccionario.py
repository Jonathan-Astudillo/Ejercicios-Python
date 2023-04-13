# Definiendo diccionarios
alumnos = {
        'nombre': "Jonnathan",
        'apellido':"Astudillo",
        'cedula':"0506873423",
        'direccion':"Ciudadela Kennedy",
        'email':"jonathan69@gmail.com"
        }
print("Mis datos son:",alumnos)

print(alumnos["cedula"])

print(alumnos["email"])
#cambiar tipo de dato
alumnos["cedula"]="06974y7338"
#agregar un dato mas al diccionario
alumnos["genero"]="Masculino"
print(alumnos)


instituto={
    'carrera':["BigData","Desarrollo de software","Cyber","Entrenamiento deportivo","Electricidad","Desarrollo Integral"],
    'materias':["Matematicas","Base de Datos","Base de Datos no Relacionales","lenguaje y Comunicacion","Introduccion a bigdata","Estadistica"],
    'profesores':["Hecto Mejia","Paul Coronel","Diana Romero","David Reinoso","Veronica Segarra","Sandra Carrera"],
    'notas':[10,8,9,7,5,4]

}
print(instituto)
print(instituto["carrera"])
print(instituto["materias"])
print(instituto["profesores"])
print(instituto["notas"])

#####promedio
suma=0
for e in instituto["notas"]:
    suma += e
    ###usar round para dejar con dos decimales
print(round(suma/len(instituto["notas"]),2))

####nota minima de las notas
print(min(instituto["notas"]))
print(max(instituto["notas"]))

print("La posicion de la nota minima\n\t",instituto["notas"].index(min(instituto["notas"])))
print("El profesor:\n\t",instituto["profesores"][instituto["notas"].index(min(instituto["notas"]))])
print("La materia es:\n\t",instituto['materias'][instituto["notas"].index(min(instituto["notas"]))])





