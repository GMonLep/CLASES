"""EJERCICIO 1 Validación de usuarios

Creen un programa que la lectura de un archivo CSV llamado 'datos.csv' que contiene
información sobre personas, incluyendo su nombre, edad y comuna. Para cada registro
en el archivo, se evalúa la edad y se determina si la persona es mayor o menor de edad.
La información, que incluye el nombre, la edad, el estado de edad y la comuna, se
imprime en la consola. Además, los registros de personas mayores o iguales a 25 años se
recopilan en una lista llamada mayores. La lista con usuarios mayores o iguales a 25 años
se guarda en un archivo JSON llamado 'mayores.json', se adjunta el conjunto de datos a
incorporar en datos.csv"""

import csv; #-->se crea un archivo csv
"""Un archivo CSV (Comma-Separated Values) es un formato de archivo que se utiliza para almacenar datos tabulares (datos en forma de tabla) en un formato de texto plano, En un archivo CSV, cada línea del archivo representa una fila de datos, y las columnas están separadas por un carácter delimitador, comúnmente una coma (,))"""

with open("datos.csv", 'w') as documento_csv:
    escritor_csv = escritor_csv(documento_csv);
    escritor_csv.writerow(campos);
    escritor_csv.writerows(filas)

diccionario_datos=[{"Nombre":"Juan","Edad":"21","Comuna":"Puente Alto"},{"Nombre":"María","Edad":"30","Comuna":"Concepción"},{"Nombre":"Carlos","Edad":"22","Comuna":"Viña Del Mar"},{"Nombre":"Estela","Edad":"25":"Puerto Montt"}];

nombre_campo=["Nombre","Edad","Comuna"];

with open("datos.csv", "w", newline="") as archivo_csv:
    writer = csv.DictWriter(datos.csv, fieldnames=fields)

