#2.2.3 Guía Ejercicios Resueltos

#EJERCICIO I: Ordenar los códigos en pantalla (AVA)
print(f"---Detalles Anualidad Colegio---")
nomAlum=input("Ingrese el nombre del alumno: ")
rut=input("Ingrese RUT apoderado: ")
curso=input("Ingrese curso al cual el alumno debe matricularse: ")
matricula=int(25000)
mensualidad=int(30000)
resultadoAnual=(mensualidad*10)+matricula
datos=(f"NOMBRE ALUMNO: {nomAlum}",f"RUT APODERADO: {rut}",f"CURSO MATRICULADO: {curso}",f"VALOR MATRICULA: {matricula}",f"VALOR MENSUALIDAD: {mensualidad}",f"VALOR TOTAL A PAGAR: {resultadoAnual}")
separador='\n'
datillos=separador.join(datos)
print(datillos)

#EJERCICIO II: ¿Por qué se ocupa float?
#ValorNetoDeUnProducto
producto=input("Ingrese el nombre del producto: ")
valorProducto=int(input("Ingrese el valor del producto: "))
valorNeto=float(0.81)
valorSinIVA=float(valorProducto*valorNeto)
datos2=(f"-----Detalle producto-----",f"NOMBRE PRODUCTO: {producto}",f"VALOR PRODUCTO: {valorProducto}",f"VALOR PRODUCTO SIN IVA: {valorSinIVA}")
datillos2=separador.join(datos2)
print(datillos2)


