def obtener_suma():
    """
    Esta funcion suma 2 elementos.
    No recibe argumentos.
    Si retorna un valor
    """
    numero1=5;
    numero2=50;
    return numero1+numero2;
print(f"La suma es: obtener_suma()");

#Ejemplo de funcion con argumentos y sin retorno
def escribir_archivo(nombre_archivo,contenido):
    """
    Recibe 2 argumentos: nombre del archivo y su contenido.
    Escribe el contenido en el archivo
    """
    with open(nombre_archivo, "w") as archivo:
         archivo.write(contenido);
    print(f"Contenido escrito en {nombre_archivo}");

#solicitamos el nombre
nombre_archivo=input("Ingresa el nombre del archivo");
#llamamos a la funcion 
contenido=input("Ingresa el contenido del archivo");

#llamos a la función
escribir_archivo(nombre_archivo, contenido);

#ejemplo funcion con retorno y argumentos
def leer_archivo(nombre_archivo):
    """
    Toma el nombre del archivo como argumento
    Lo lee
    Retorna el contenido del archivo.
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido=archivo.read();
            return contenido;
    except FileNotFoundError:
        return "El archivo no fue encontrado";


#llamamos a la funcion leer y guaardamos el contenido
contenido_archivo=leer_archivo(nombre_archivo);
#imprimir el contenido del archivo
print(f"Contenido de {nombre_archivo}:\n{contenido_archivo}");

#funcion con argumento y con retorno
def contar_palabaras(contenido):
    #Esta funcion recibe el contenido y cuenta las palabras en la cadena.
    palabras=contenido.split();
    return len(palabras);

#llamamos a la funcion para contar palabras y guarda el resultado.
numero_palabras=contar_palabaras(contenido_archivo);
#Imprimimos el resultado
print(f"El archivo {nombre_archivo} tiene {numero_palabras} palabras.");

#funcion para contar lineas
def contar_lineas(contenido):
    #Recibe una cadena como argumento y cuenta las líneas totales.
    lineas=contenido.split('\n');
    return len(lineas);

#llamamos a la función
numero_lineas=contar_lineas(contenido_archivo);
#imprime el numero de lineas
print(f"El archivo {nombre_archivo} tiene {numero_lineas} líneas.");
#funcion para contar caracteres
def contar_caracteres(contenidos):
    #Esta funcion cuenta cada caracter del contenido
    return len(contenido);

#llamamos a la funcion
numero_caracteres=contar_caracteres(contenido_archivo);
#imprimir
print(f"El archivo {nombre_archivo} tiene {numero_caracteres} caracteres.");

#funcion que busca una palabra
def buscar_palabra(contenido):
    """Esta funcion toma como argumentos el contenido
    Retorna el numero de veces de la palabra en el contenido"""
    return contenido.lower().split().count(palabra.lower());

#solicitamos la palabra a buscar
palabra=input("Ingresa la palabra a buscar: ");

print(f"La palabra {palabra} aparece {apariciones} veces en el archivo");

def validar_entrada(mensaje):
    """Toma una cadena como argumento. 
    Retorna la entrada validada.
    """
    while true:
        entrada=input(mensaje);
        if entrada.script():
            return entrada
        else:
            print("Error: Entrada no válida, intente nuevamente");
        
#Solicitamos el nombre del archivo y el contenido a validar
nombre_archivo2=validar_entrada("Ingrese el nombre del archivo a leer")

#llamamos a la funcion leer archivo y guarda el contenido
contenido_archivo2=leer_archivo(nombre_archivo2);

#verificar si el archivo fue leido correctamente
if "Error" not in contenido_archivo2:
    numero_palabras=contar_palabras(contenido_archivo2);
    print(f"Contenido de {nombre_archivo2}:\n{contenido_archivo2}");
    print(f"El archivo {nombre_archivo2} tiene {numero_palabras} palabras.");

    