#1)Calcular los días de vida en base a la edad

edad=int(input("INGRESA TU EDAD PARA TRANSFORMARLA EN DIAS:" ))
bisiesto = edad//4
#// aproxima el decimal al n° más pequeño, mientras que / da décimal
#round es redondear al n° mayorr
dias = edad*365
definitivo= dias+bisiesto
print("TU EDAD EN DIAS ES ", definitivo)

#2)Crear una calculadora básica + - * / con funciones

decision=int(input("QUE QUIERES HACER (1.sumar, 2.restar, 3.dividir, 4.multiplicar)"))
numeroUno = int(input("PON TU PRIMER NUMERO, INMUNDO ANIMAL"))
numeroDos = int(input("PON TU OTRO NUMERO"))

if decision==1:
   def sumar():
    sumar=numeroUno+numeroDos
    print ("TU resultado es: ", sumar)
 sumar ()

if decision==2:
   def restar():
    restar=numeroUno-numeroDos
    print ("TU resultado es: ", restar)
 restar ()

def multiplicar ():
    multiplicar=numeroUno*numeroDos
    print ("TU resultado es: ", multiplicar)
 multiplicar()

def dividir ():
    dividir=numeroUno/numeroDos
    print ("TU resultado es: ", dividir)
 dividir()



