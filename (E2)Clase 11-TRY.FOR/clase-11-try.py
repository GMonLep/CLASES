#ejemplo de una division utilizando try (encapsular y detectar tipo de error):


def dividir(numero1,numero2):
    try:
        resultado=numero1/numero2;
        print(f"el resultado de la division es: {resultado: .0f}"); #para sin decimal, f=a que es un num flotante
    except ZeroDivisionError:
        print("no se puede dividir x cero");
    except TypeError:
        print("dato ingresado no valido");
    else: 
        print("la division se ejecuto correctamente");
    finally:
        print("fin del programa");

numero1=input("ingresa un numero sanababich: ");
numero2=input("ingresa otro numero moterfoker: ");
dividir(numero1,numero2);

