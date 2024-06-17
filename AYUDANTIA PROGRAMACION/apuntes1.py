#declarar variables
a=2;
b=1;

#sentencia de condicion

if(a>b): #el : es como el entonces d pseint
    print("a es mayor que b"); #el ; no es necesario en python pero si en JAVA
elif(b>a):
    print("b es mayor que a");
else:
    print("son iguales");

#EJERCICIO
edad=int(input("Escribe tu edad, maldito animal: "));
if (edad>=18):
    print("USTE E MAYOR DE EDADDD");
elif (edad>0) and (edad<18):
    print("nooo eres mayor d edaaa");
else:
    print("pon una edad como la gente pooo")

#EJERCICIO2
user_1="pedro";
pass_1="1234";
user_2="angel";
pass_2="a4s1";

user=input("ponga su nombre de usuario");
password=input("pone tu contraseñaaa");

if (user==user_1 and password==pass_1) or (user==user_2 and password==pass_2):
    print ("holiii")
else:
    print("acceso denegado");

#ejercicio4
australiano=0.0016; #1 peso chileno q es en australia
yen=6.04;
argentino=1.07;


money=float(input("PONga la plata chilena a convertirr "));
decision=int(input("¿A que queris convertir? \n 1.a dolar australiano \n 2.yen japoness \n 3.peso argentino che \n metale bueno: "));

if (decision==1):
    r1=money*australiano;
    print(r1);
elif (decision==2):
    r2=money*yen;
    print(r2)
elif (decision==3):
    r3=money*argentino;
    print(r3)
else:
    print("acaso no sabes leer ahi decia escoje del 1-3")