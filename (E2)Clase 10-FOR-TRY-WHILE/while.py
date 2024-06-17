#adivina el numero generado aleatoriamente
#importamos la libreria random
import random;
numero_secreto=random.randint(0,100);
#print(numero_secreto);

intentos=0;

while True:
    intento=int(input("ingresa un  numero del 0 al 100"));
    intento+=1;
#decision para saber si es mayor o menor
    if intento<numero_secreto:
        print(f"el numero ingresado es menor al num secretou con {intentos} intento(s)");
    elif intento>numero_secreto:
        print(f"el numero ingresado es menor al num secretou con {intentos} intento(s)");
    else:
        print(f"felicidades adivinasteeeeeeeeeeeee, el num secreto era {numero_secreto}, para adivinar ocupaste {intentos} intento(s)");
    break
print("findelljuego")