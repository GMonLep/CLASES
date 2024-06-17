#ARCHIVO PRINCIPAL

#from apuntes3FUNCIONES import * #SE IMPORTAN TODAS LAS FUNCIONES DEL ARCHIVO 
import apuntes3FUNCIONES as funcion #lo mismo, sirve igual, "Usare todas las funciones como funciones"-esta es mas wena

print(funcion.sumarDosNumerosRETORNO())+100; #con esta cosa se puede elegir la funcion a llamar

"""EJERCICIO CASINO DUOC: crear algoritmo para la administracion de un casino, en un archivo hacer funciones y en otro importar.
1)funcion agregar producto
2)fincion buscar producto
3)funcion eliminar producto
4)funcion mostrar productos
5)salir"""

while True:
    print("\nInventario Casino DUOC\n");
    print("1. Agregar producto.");
    print("2. Buscar producto.");
    print("3. Eliminar producto.");
    print("4. Mostrar producto.");
    print("5. Salir.");
    #llamar a las funciones
    if(opcion==1):
        funcion.AgregarProductos();
    elif(opcion==2):
        print();
    elif(opcion==3):
        print();
    elif(opcion==4):
        funcion.MostrarProductos();
    else:
        print("Opción no válida");
