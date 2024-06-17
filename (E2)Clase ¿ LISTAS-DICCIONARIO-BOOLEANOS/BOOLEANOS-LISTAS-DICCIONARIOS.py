#Comentario de una línea.

"""
Comentarios multilinea:
 -Variable: espacio de memoria reservado que puede cambiar en el transcurso del programa.
 -Python es un lenguaje de tipo dinámico: no es necesario declarar explicitamente el tipo de variable antes de usarla. 
 El tipo de dato se infiere según el valor asignado.

"""
entero = "5"
#Para imprimir datos en Python se utiliza la funcion print( )
print (entero)

#Para saber el tipo de dato de una variable type( )
print(type(entero))

"""
Palabras reservadas en Python:
False-None-True
and-as-assert-async-await-break-class-continue-def-del-elif-else-except-finally-for
global-if-import-in-is-lambda-nonlocal-not-or-pass-raise-return-try-while-with-yield

"""
#Tipos de datos en Python

varEntero = 2
flotante = 1.75
booleanoTRUE = True
booleanoFALSE = False
cadenaTexto = "Cadenilla de textillo"

suma = 9+9
resta = 6-6
division = 9/6
multiplicacion = 6*9

print("---------")
print (suma)
print (resta)

#Concatenación de cadenas
saludo = "Hola"
nombreAlumno = "Pedro"
mensaje = saludo + " " + nombreAlumno + "¿Cómo estás?"
print (mensaje)

edad=18
es_estudiante = True
tiene_trabajo = False
#Operaciones lógicas con booleanos
es_mayor_de_edad = edad >= 18 #comprobando si la edad es mayor o igual a 10
puede_votar = es_mayor_de_edad and tiene_trabajo

print ("es mayor de edad", es_mayor_de_edad)
print ("¿Puede votar?", puede_votar)

#Listas: colecciones de datos ordenados y modificables. Pueden contener distintos tipos de datos.
#Para declarar una lita se usan corchetes []

numeros = [1,2,3,4,5,6,7,8,9] #Lista números
alumnos = ["Juan", "Fulanito", "Cosmo", "Wanda"] #Lista de cadenas
listaMixta = [1, "Hola", False, 1.2] #Lista mixta

print (listaMixta) #lista completa
print (listaMixta [2] ) #lista detallada
print (listaMixta [-2] ) #orden inverso las listas parten desde el número 1

#Tuplas: colecciones de datos ordenados e inmutables. Una vez se crean las duplas, no se pueden modificar los datos. ()

coordenadas = (10,20)
meses = ("Enero", "Febrero", "Marzo")

print(meses[2]) #Sale marzo porque no se cuenta al primer dato como 1, sino como 0: ENERO=0, FEBRERO=1, MARZO=2
print (meses [-1])

#Conjuntos: colecciones de datos desordenados y no indexados.
#Se definen de dos maneras 1 - {}  2- set ()

numerosPrimos = {2,3,4,7,11}
lenguaje = set("Python3")
#Agregar elementos a un conjunto
numerosPrimos.add (13)
lenguaje.remove("3")

print (numerosPrimos)
print (lenguaje)

#Diccionario de datos: colecciones de datos desordenados creados mediante una clave y valor {}

persona = {
    "Nombre": "Marcelo",
    "Nacionalidad": "Chileno",
    "Ciudad": "Puerto Montt",}

print (persona["Nombre"]) #Imprimir un diccionario con un dato específico

#Ahora modificar dato específico
persona["Nacionalidad"] = "Chileno"
print (persona)
Agrega nuevos datos al diccionario clave: valor 
persona ["Edad"]

curso = 20
print (curso)

#Cambiar tipo de dato
numero1= int(input("ingrese un número"))
numero2 = int(input("ingrese un número"))
suma =numero1 + numero2
print(suma)
print(type(numero1))

"""
Ejercicio 1: convertir temperatura de Farenheit a Celsius.
Ejercicio 2: calcular la edad exacta del usuario.

"""
