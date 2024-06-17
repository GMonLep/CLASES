a=5;
while (a>0):
    print (f"el valor de a es:{a}");
    a=int(input("ingrese un valor"));

try:
    num=int("abc");
    print(num);
except ValueError:
    print("error: valor no valido");

