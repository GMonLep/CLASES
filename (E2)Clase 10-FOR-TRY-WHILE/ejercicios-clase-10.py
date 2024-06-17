"""
EJERCICIO 1
Realiza construcción de un programa que deba realizar lo siguiente:
Comienza con la inicialización de variables y solicita al usuario la cantidad de bultos. Luego, utiliza un bucle FOR para procesar cada bulto, solicitando el peso al usuario y manejando posibles errores (agregar excepciones). Dependiendo del peso ingresado, acumula valores y contadores correspondientes para bultos livianos y normales. Finalmente, imprime el total a pagar por bultos livianos y normales, así como la cantidad de bultos en cada categoría.

Una empresa de transporte requiere automatizar sus procesos de cálculo para poder cobrar por la cantidad de paquetes que trae un cliente.
Para calcular el valor total a cobrar y catalogarlo para envío, requiere preguntar elpeso de cada bulto y determinar el valor según lo siguiente:

Kilos     Categoría    Valor
1 - 5      Liviana    $1,000
6 - 10     Normal     $2,000

Ejemplo:
Si un cliente ingresa 3 bultos y según sus pesos estos clasifican en 1 liviano y 2 normales, el cliente debe paga $5,000
El sistema debe mostrar lo siguiente:
1 bulto liviano $1,000
2 bultos normales $4,000
Valor total a pagar: $5,000
"""

cantidad_bultos=int(input("ingrese cantidad de bultos a transportar"));
while cantidad_bultos:
    bulto=float(input("cuanto pesa (kg): "));

for bulto in range(0,6):
    categoria="liviano(s)";
    valor=1000;
valor1=bulto*valor
print(f"{cantidad_bultos} bulto(s) {categoria} serían {valor1}")
for bulto in range (5,11):
    categoria="normal";
    valor=2000;

