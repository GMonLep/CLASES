#Ejercicios básicos para prácticar con Python (2)

#1)Calculadora de IMC:
nombre=input("Este es un calculador del índice de masa corporal (IMC). Por favor ingrese su nombre: ")
peso=int(input("Ingrese su peso (kg), por favor escriba solo el número: "))
altura=float(input("Ingrese su altura (kg), si desea usar una coma, reemplacela por un punto: "))
IMC=peso/(altura**2)
redondeo=(round(IMC,2))
print(f"{nombre}, tu IMC corresponde a {redondeo}.")
