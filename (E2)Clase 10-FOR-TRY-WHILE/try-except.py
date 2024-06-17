#para encapsular codigos donde queremos evaluar si tiene o no errores
try:
    resultado=10/0 #generamos el error para ver como funciona except
    print(f"el resltado de la divison es {resultado}");
except ZeroDivisionError:
    print ("error no se puede divir por cero");
