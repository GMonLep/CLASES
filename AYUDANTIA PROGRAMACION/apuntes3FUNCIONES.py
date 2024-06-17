#Funcion en python: todo lo que tiene parentesis

#def() #--> sirve para definir una funcion
#return #---> palabra definida para devolver una funcion

""""Hay funciones 
con retorno: se espera que se devuelva algo
sin retorno: cumple alguna labor, quiza cambiar algo 
con parametros: entregarle algo con parentesis para saber si recibe algo
"""

#una funcion que le das una serie de tareas para hacer, puedes llamarla o no llamarla
#FUNCION SIN PARAMETROS SIN RETORNO
def sumarDosNumeros():
    N1=int(input("INGRESE UN N°: "));
    N2=int(input("INGRESE OTRO N°: "));
    resultado=N1+N2
    print(resultado);

#FUNCION CON PARAMETROS Y SIN RETORNO

def sumarDosNumerosPARAMETROS(N1,N2):
    resultado=N1+N2;
    print(resultado);

#llamar funcion creada
num1=int(input("INGRESE UN N°: "));
num2=int(input("INGRESE OTRO N°: "));
sumarDosNumerosPARAMTROS(num1,num2)

#FUNCION SIN PARAMETROS Y CON
def sumarDosNumerosRETORNO():
    N1=int(input("INGRESE UN N°: "));
    N2=int(input("INGRESE OTRO N°: "));
    resultado= N1+N2;
    return resultado
    print(resultado);

#funcion con parametros y con retorno
def sumarDosNumerosPARAMETROSRETORNO(num1,num2):
    resultado=num1+num2;
    return resultado;


print(sumarDosNumerosPARAMETROS()+300+200)

"""EJERCICIO CASINO DUOC: crear algoritmo para la administracion de un casino, en un archivo hacer funciones y en otro importar.
1)funcion agregar producto
2)fincion buscar producto
3)funcion eliminar producto
4)funcion mostrar productos
5)salir"""

lista_productos=["Lays","Crispo","Chocman","Super 8"];

def AgregarProductos():
    producto=input("Ingrese el nombre del producto: ");
    if producto not in lista_productos:
        lista_productos.append(producto);
        print("Producto ingresado correctamente");
    else:
        print("El producto ya está en la lista. No se agregó nada.");



def MostrarProductos():
    print(lista_productos);
