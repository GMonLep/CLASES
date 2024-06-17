saldo=500000;
sw=6

while sw==6:
    print("Menu de opciones:\n  1. Ver mi saldo\n  2. Retirar dinero\n  3. Salir\n");
    opcion=int(input("Ingrese una opción:  "));
    if opcion==1:
        print(f"Tu saldo es ${saldo}.")
        ws=1
        while ws==1:
            decision=int(input("\nPresiona 1 para volver al menú de opciones o 2 para salir:  "));
            if decision==1:
                print("Volviendo...\n")
                ws==!
            elif decision==2:
                ws=2
                sw=9
                print("Cierre de sesión exitoso, adiós.")
            else:
                print("Escoja una opción válida.")
    if opcion==2:
        print("\nTransferencia realizada");
        ws=1
        while ws==1:
            decision=int(input("\nPresiona 1 para volver al menú de opciones o 2 para salir:  "));
            if decision==1:
                print("Volviendo...\n")
                ws==2
            elif decision==2:
                ws=2
                sw=9
                print("Cierre de sesión exitoso, adiós.");
            else:
                print("Escoja una opción válida.")
    if opcion==3:
        print("Cierre de sesión exitoso, adiós.");
        break;
    else:
        print("Escoja una opción válida.");