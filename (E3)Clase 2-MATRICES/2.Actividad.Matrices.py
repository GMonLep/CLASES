"""
1. Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla
utilizando doble for, mostrar los elementos por pantalla de forma ordenada como
una matriz, tal cual muestra el ejemplo:
3 10 4 16
1 7 8 -7
9 -1 3 9
"""
matriz1=[
   [3,10,4,16],
   [1,7,8,-7],
   [9,-1,3,9],
];

for fila in matriz1:
        print(fila,"\n",end=" ");

"""2. Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser
'amarillo', 'rojo', 'Naranja', 'Verde' y 'Blanco'.
Una vez completado, mostrar la siguiente información:
● Número de elementos 'amarillo'.
● Número de elementos 'rojo'.
● Número de elementos 'Naranja'.
● Número de elementos 'Verde'.
● Número de elementos 'Blanco'"""

matriz_colores=[
        ["amarillo", "rojo", "naranja"],
        ["verde", "blanco", "rosa"],
        ["morado", "negro", "azul"]
];
for fila in matriz_colores:
    for elemento in fila:
         print(f"Número de elementos: '{elemento}' \n", end=" ")


"""3. Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma
automática los números de asiento y luego mostrarlo por pantalla
de la siguiente forma
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
21 22 23 24
25 26 27 28
29 30 31 32
33 34 35 36
37 38 39 40"""

matriz_muchos=[
      [1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16],
      [17,18,19,20],
      [21,22,23,24],
      [25,26,27,28],
      [29,30,31,32],
      [33,34,35,36],
      [37,38,39,40]
]

print(matriz_muchos)