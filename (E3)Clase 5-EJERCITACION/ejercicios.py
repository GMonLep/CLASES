"""Caso 1: Nombre con Mayor Cantidad de Caracteres
Escriban un programa en Python que permita a los usuarios ingresar 3 nombres por
pantalla y almacenarlos en una lista. Luego, el programa debe determinar y mostrar el
nombre que tiene la mayor cantidad de caracteres en un mensaje de salida por pantalla."""
nombre1=input("Ingrese el primer nombre: ");
nombre2=input("Ingrese el segundo nombre: ");
nombre3=input("Ingrese el tercer nombre: ");

lista_nombres=(nombre1,nombre2,nombre3);
print(f"El nombre más largo es: {max(lista_nombres, key=len)}); #by using 'key=len' we tell it to get the key with the maximum lenght(len)

"""Caso 2: Nombres y Apellidos Ordenados
Creen dos listas, una para nombres y otra para apellidos. Almacenen 3 nombres y 3
apellidos en estas listas. Luego, muestren de forma ordenada los nombres y apellidos."""

nombre1=input("\nNombre: ");apellido1=input("Apellido: ");
nombre2=input("\nNombre: ");apellido2=input("Apellido: ");
nombre3=input("\nNombre: ");apellido3=input("Apellido: ");


"""Caso 3: Agregar Nombres y Eliminar el Menos Extenso
Creen un programa que permita almacenar nombres en una lista. El sistema debe
preguntar si desean agregar otro nombre y seguir permitiendo la entrada de nombres
hasta que la respuesta sea "no". Después de ingresar n nombres, eliminen el nombre con
la menor cantidad de caracteres."""