#Saldo inicial en cuenta
saldo = 100000 #Loop principal del programa
while True:
    #Mostrar menú
    print("bienvenido. seleccione una opcion\n1. consultar saldo\n2. retirar dinero\n3. salir")
    #solicitar una opcion al usuario
    opcion= input("selecciona una opcion(1-3)")
    #realizar acciones segun opcion que corresponda
    if opcion=="1":
        print(f"tu saldo actual{saldo}")
    elif opcion=="2":
        cantidad_a_retirar=float(input("íngrese la cantidad q quieres sacar: $"))
        if cantidad_a_retirar<=saldo:
            saldo-=cantidad_a_retirar;
            print(f"retiraste ${cantidad_a_retirar}. nuevo saldo: ${saldo}")
        else:
            print("saldo insuficiente, no se pudo hacer retiro")
    elif opcion=="3":
        print("gracias por usar cajero")
        break
    else:
        print("opcion no valida, por favor escoja una opcion válida")
