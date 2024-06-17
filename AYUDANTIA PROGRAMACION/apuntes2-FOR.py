#declarar variables
#for con u Range (x)

rango=range(5);
for i in rango:
    print(f"El valor de i es: {i}");

#for con una cadena de texto
texto="Génesis";
for i in texto:
    print(f"El valor de i es: {i}");

#for utilizando una lista
lista_nombres=[];
lista_nombres.append("Juan"); #---> la diferencia con el insert es que el insert te permite escojer la posicion en la que agregar el valor, en cambio el append por defecto lo pone uno despues de otro
lista_nombres.append("Francisca");
lista_nombres.append("Panchita");
lista_nombres.append("Fran");
lista_nombres.append("Cisca");

for i in lista_nombres:
    print(f"El valor de i es {i}");

#for utilizando una matriz 
print("\nFor utilizando una matriz\n");
matriz_numerica=[[1,2,3],
                 [4,5,6],
                 [7,8,9]];
for i in matriz_numerica:
    print(f"El valor de i es {i}");

for i in matriz_numerica:
    print(f"La lista es: {i}");
    for valorcillo in i:
        print(f"el valor cada elemento en la lista es: {valorcillo}");

"""Crear un algortmo que almacene una listo los números de una tabla de multiplicar de acuerdo al número ingresado por el teclado.
3 - [3,6,9,12,15,18,21,24,27,30]"""

lista_multiplicar=[];
numeros_multiplicar= [1,2,3,4,5,6,7,8,9];

numero=int(input("Ingrese un número: "));


"""Crear un algoritmo que permiat ingresar 3 nombrs y almacenarlos en una lista. Luego, debe immprimir en pantalla, el nomrb que tenga la mayor cantidad de caracteres"""
