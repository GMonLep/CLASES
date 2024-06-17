#EJERCICIOS 29-04-2024

#.lower() --> pone todo en minuscula para que sea más fácil validarlo despues

"""
EJERCICIO 1: Descuento por edad
Reordenar los códigos con el fin que el sistema valide:
 -Rango de edad entre 0 y menor que 18 años. Descuento de 50%.
 -Rango de edad entre 18 y menor que 30 ñños. Descuento de 20%.
 -Mayor o igual a 60 años. Descuento de 90%.
"""
edad= int(input("Ingrese su edad \n"));
if 0<edad and edad>18:
    print(f"Edad: {edad}, tiene descuento en un 50%");
elif edad>=18 and edad<30:
    print(f"Edad: {edad}, tiene descueno de un 20%.");
elif edad>=60:
    print(f"Edad: {edad}, tiene descuento de un 90%.")
else:
    print(f"Edad: {edad}, no aplica descuento.")

"""
EJERCICIO 2: validación user y pass
  -¿Qué sentencia de igualdad debemos utilizar para que el sistema de la bienvenida al usuario cuando el usuario ingrese el user y pass correcto? 
"""
validUser="gesita";
validPass="bonita";

user=input("Ingrese su usuario \n");
pwd=input("Ingrese su contraseña \n");

if user==validUser and pwd==validPass: #sentencia faltante (recordar que el == es para igual y = para igual en operaciones matemáticas.)
    print("BIENVENIDO LARVAAAAAAAAAAAAAAAA");
else:
  print("contraseña o usuario incorrecta, sal de aqui inmundo animal");

"""
EJERCICIO 3: Devolución dinero
¿Qué mensaje nos imprimirá el sistema, si nos devuelve una devoluciónde dinero de $120.000, e ingresamos el user “duoc123”, y el pass“123duoc”?
"""
user=input("Ingrese el usuario: \n");
pwd=input("Ingrese la contraseñisima: \n");

if user=="duocuc" and pwd=="123duoc":
    valorDev=int(input("Bienvenido, ingrese el valor a devolvers: \n"));
    if valorDev>100000:
        print("Nos vamos a apurar")
    else:
        print("pucha...ya...altiro lo vemos... ahi quedo registrado");
else:
    print("no se que hiciste pero algo esribiste mal puede ser el usuario o la contraseña mano");