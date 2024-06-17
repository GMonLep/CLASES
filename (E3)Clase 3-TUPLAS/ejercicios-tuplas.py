"""Ejercicio 1: Información Personal
Objetivo: Practicar la creación y acceso a elementos de tuplas.
1. Crea una tupla llamada `informacion` que contenga los siguientes elementos en orden: tu
nombre, tu edad, y tu ciudad de residencia.
2. Accede e imprime cada elemento de la tupla utilizando índices.
3. Utiliza el desempaquetado de tuplas para asignar los valores a variables individuales y
luego imprime estas variables."""

informacion=("Pedro", "54", "Gotham");
print(f"Nombre: {informacion[0]}\nEdad: {informacion[1]}\nCiudad de residencia: {informacion[2]}");

"""
Ejercicio 2: Operaciones con Tuplas Numéricas
Objetivo: Practicar el uso de funciones y métodos con tuplas.
1. Crea una tupla llamada `numeros` que contenga los números del 1 al 10.
2. Utiliza la función `sum()` para calcular la suma de los elementos de la tupla.
3. Utiliza las funciones `max()` y `min()` para encontrar el valor máximo y mínimo en la tupla.
4. Utiliza el método `count()` para contar cuántas veces aparece el número 5 en la tupla."""

numeros=(1,2,3,4,5,6,7,8,9,10);
print(sum(numeros))
print(f"El número máximo de la tupla es {max(numeros)} y el número mínimo de la tupla: {min(numeros)}");
print(f"El número 5 aparece {numeros.count(5)} vez en la tupla.");

"""Ejercicio 3: Rebanado de Tuplas
Objetivo: Practicar el rebanado (slicing) para obtener sub-tuplas.
1. Crea una tupla llamada `letras` que contenga las letras del alfabeto de la 'a' a la 'j'.
2. Utiliza el rebanado (slicing) para obtener una sub-tupla con las primeras 5 letras e
imprímela.
3. Utiliza el rebanado para obtener una sub-tupla con las últimas 3 letras e imprímela.
4. Utiliza el rebanado con pasos (saltos) para obtener una sub-tupla con cada segunda letra
e imprímela.
¡Buena suerte y a practicar!"""

letras=("a","b","c","d","e","f","g","h","i","j");
print(f"Resultado del slicing 5 primeras letras: {letras[0:5]}");
print(f"Resultado slicing últimas 3 letras: {letras[7:10]}");
sub_tupla=(letras[1:10:2]);
#           [start:finish:step of incrementation]
print(sub_tupla);