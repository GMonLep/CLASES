#Números complejos 
numeroComplejo=1j
print(type(numeroComplejo))

#Datos de tipo rango range
coordenadas = range(9)
print(coordenadas)
print(type(coordenadas))

#Datos set() Conjunto: tipo de dato que ofrece prints desordenados

numeros={2,3,4,5,7,9}
numeros.add(13) #--> numero agregado al conjunto, se agrega al final
letras = set("Python3")
letras.remove("3") #--> numero que se le quita al conjunto
print(type(letras))

"""
Frozenset: Es una colección inmutable parecida a un set, es inmutable/ comandos remove o add no se puelen usar
"""
frutas = frozenset ({"Arándanos", "Frutilla", "Manzana Roja", "Manzana Verde"})
print(frutas)
print(type(frutas))

"""
Bytes: es un tipo de dato inmutable, que parte del 0-255.
"""
#Crear un objeto a partir de un bytes

variableBytes=bytes("hola holis holaa", "utf-8") #utf-8: codificacion para carácteres "especiales", como la ñ, tildes--> cada lenguaje tiene su codificacion especifica, si se quisieran usar simbolos rusos seria otra codificacion.
print(variableBytes)#-->aparece una b al principio para indicar que es una variable bytes

#Crear un texto a partir de números bytes
b=bytes([72,111,108,97])
print(b)

#byteArray
c=bytearray("Hola que tal", "utf-8")
print(c)

#modificar un byteArray
c[0]=83
print(c)

#Datos d etipo None: es un tipo de dato unico que no respresenta un valor.
variableNone= None
print(variableNone)

#
hola = "hola amix"
print(hola[5:9])
print('hola "DUOC"')