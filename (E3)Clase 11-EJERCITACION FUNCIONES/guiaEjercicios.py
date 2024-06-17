"""EJERCICIO 1 Calculadora con funciones
Creen un programa que emule la función de una calculadora, debe tener 4 funciones,
sumar, restar, dividir y multiplicar, el programa de permitir el ingreso de dos números de
tipo enteros. Este programa debe contener una pequeña validación que indique un
mensaje cuando se divide por 0, indicado que no se puede realizar la operación. Las
funciones a construir deben ser con argumentos y con retorno."""

def funcion_suma(a,b):
    resultado=a+b;
    return print(f"={resultado}");

def funcion_resta(a,b):
    resultado=a-b
    return print(f"RESULTADO RESTA = {resultado}");
    
def funcion_multiplicacion(a,b):
    resultado=a*b
    return print(f"RESULTADO MULTIPLICACIÓN = {resultado}");

def funcion_division(a,b):
    try:
        resultado=a/b
        return resultado
        print(f"RESULTADO= {resultado}")
    except ZeroDivisionError:
        print("ERROR: NO SE PUEDE DIVIDIR POR CERO.")



