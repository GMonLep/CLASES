"""
ACTIVIDAD 1
a) Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
"""
edad=int(input("Buenos dias buenas tardes, ingrese su edad pls\n"));
if edad>=18 and edad<122 :
    print("usted es mayor d edaad");
elif 0<edad<18:
    print("mocoso asqueroso fuera de aqui");
elif edad>122:
    print("imposible, la persona más longeva documentada fue Jeanne Calment y se murio en 1997, no mientas");
elif edad<0:
    print("pon una edad enserio");
else:
    print("no te pesco");
    
"""
b) Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
-User1: pedro Contraseña1: 1234
-User2: angel Contraseña2: a4s1
Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla 'Aprobado' en el caso de que el promedio sea igual o mayor a 4.0.
"""
user1="pedro";
pw1="1234";
user2="angel";
pw2="a4s1";

user=input("Wena larvaaa, ingresa tu usuario larvaaa\n");
pw=input("Ingresa tu contraseña larvaaaa\n");
if user==user1 and pw==pw1 or user==user2 and pw==pw2:
    print("bienvenido larvaaa, calculemos tu promedio larvaaa\ningresa tus notas larvaaaaa, solo 3 larvaaaa");
    nota1=float(input());
    nota2=float(input());
    nota3=float(input());
    promedio=round((nota1+nota2+nota3)/3);
    print(f"tu promedion essssssssss {float(promedio)}."); 
    if 4.0<=promedio<=7.0:
        print("APROBASTE LARVAAAAAAAA");
    elif 1.0<promedio<4.0:
        print("pucha... reprobaste po mano");
    else:
        print("las notas en chile van del 1.0 al 7.0 porsiacasooo, alguna pusiste mal porque el resultado no cuadra")

else:
    print("INGRESO NO AUTORIZADO\na LO mejor pusiste mal tu usuario o tu contra amix");

"""
c) Crear una salida por pantalla con la siguiente información: ¿Cuál de los siguientes animales vive en el agua?
Perro
Cocodrilo
Conejo
Tiburón
Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la respuesta es Tiburón asignar +1.0 a puntaje, del cualquier otro caso, no asignar valor, finalmente crear una salida por pantalla para mostrar el puntaje obtenido.
"""

respuesta=input("¿Cuál de los siguientes animales vive en el agua?\n1.Perro\n2.Cocodrilo\n3.Conejo\n4.Tiburón\n4.Ver resultados\nRespuesta: ");
while respuesta!="4":
    input=