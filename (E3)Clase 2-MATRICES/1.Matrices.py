"""
¿Qué es una matriz?
Estructura de datos que puede tener múltiples dimensiones.           

----> es fila
|
|
v
#es columna

cmo se usa
  - Matriz unidimensional vs bidimensional y tridimensional"""

#matriz UNIDIMENSIONAL o VECTOR: está en un fila o una columna
matriz_1D= [1,2,3,4,5,6,70];
  
#acceder a fila especifica:
elemento_matriz1D= matriz_1D[0];
print(elemento_matriz1D); #--> los print son pa' corroborar

#modificar un elemento:
matriz_1D[6]=7;
print(matriz_1D);

#agregar un elemento a la matriz:
matriz_1D.append(8);
print(matriz_1D)

#eliminar un elemento:
matriz_1D.remove(8);

matriz_desorden= [2,4,6,8,3,0,9];
#ordenar matriz
matriz_desorden.sort();
print(matriz_desorden)

#matriz BIDIMENSIONAL: lista de listas, cada elemento dentro de la matriz es otra matriz
matriz_2D=[
 [1,2,3],
 [4,5,6]
]
#acceder a un elemento en particular dentro de la matriz bidimensional:
elemento_matriz_2D= matriz_2D[1][2];
print(elemento_matriz_2D);

#modificar un elemento en especifico:
matriz_2D[1][2]=7;
print(matriz_2D);

#recorrer una matriz bidimensional:
for fila in matriz_2D:
    for elemento in fila:
        print(elemento);

#matriz MULTIDIMENSIONAL: extiende el concepto de matriz multidimencional a más dimensiones.

matriz_3D = [
    [
        [1,2,3],     #primer corchete morado es 0
        [4,5,6]
    ],
    [
        [7,8,9],       #segundo corchete morado es 1
        [10,11,12]
    ]       
]
print(matriz_3D);

#acceder a un elemento especifico:
elemento_3D=matriz_3D[1][1][2];
print(elemento_3D);

#recorrer una matriz tridimensional:
for dimension in matriz_3D:
    for elemento in dimension:
        for fila in elemento:
            print(fila)
