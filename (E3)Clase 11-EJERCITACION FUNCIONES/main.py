"""EJERCICIO 1 Calculadora con funciones
Creen un programa que emule la función de una calculadora, debe tener 4 funciones,
sumar, restar, dividir y multiplicar, el programa de permitir el ingreso de dos números de
tipo enteros. Este programa debe contener una pequeña validación que indique un
mensaje cuando se divide por 0, indicado que no se puede realizar la operación. Las
funciones a construir deben ser con argumentos y con retorno."""

import guiaEjercicios as funcion

while True:
    print("CALCULADORA")
    print("1. SUMAR");
    print("2. RESTAR");
    print("3. MULTIPLICAR");
    print("4. DIVIDIR");
    print("5. SALIR");
    decision=int(input("Eliga una opción: "));
    if (decision==1):
        print("INGRESE LOS NÚMEROS:");
        num1=int(input());
        print()
        num2=int(input("+"))
        print(funcion.funcion_suma(num1,num2));
    elif (decision==2):
        num1=int(input("end="""));num2=int(input("-"))
        print(funcion.funcion_resta(num1,num2));
    elif (decision==3):
        num1=int(input("end="""));num2=int(input("*"))
        print(funcion.funcion_multiplicacion(num1,num2));
    elif (decision==4):
        num1=int(input("end="""));num2=int(input("/"));
        print(funcion.funcion_division(num1,num2));
    elif (decision==5):
        print("Saliendo...")
        import os
        import time
        time.sleep(3)
        os.system('cls')
        break
    else:
        print("INGRESE UNA OPCIÓN VÁLIDA");
        
num1=int(input())
num2=int(input())
print(funcion.funcion_division(num1,num2));