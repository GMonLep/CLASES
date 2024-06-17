#Función anidada: una funcion dentro de otra
#Organizar el codigo
def operacion_anidada(a,b):
    def suma(n1,n2): #--> a seria n1 y b seria n2
        return n1+n2;
    def multiplicacion(n1,n2):
        return n1*n2;
    resultado_suma=suma(a,b);
    resultado_multiplicacion=multiplicacion(a,b);
    return resultado_suma, resultado_multiplicacion;

#LLamar a mi función:
resultado_suma, resultado_multiplicacion=operacion_anidada(4,5);
print(f"La suma de 4 y 5 es {resultado_suma}, y su multiplicación es {resultado_multiplicacion}.")

#Función de tipo lambda: funcion de tipo anonima por si te da flojera darle nombre a tu funcion
#Elevaremos numeros al cuadradado esta vez
elevar_cuadrado=lambda x:x**2
#Lista de números
numeros=[1,2,3,4,5]
#Usar la funcion map() va a aplicara mi funcion lambda a cada numero de mi lista
#list() convierte cada numero o resultado a una lista
numeros_cuadrados=list(map(elevar_cuadrado,numeros));
print(f"Los números: {numeros} elevados al cuadrado son: {numeros_cuadrados}");