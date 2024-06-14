import os, time



trabajadores = []

while True:
    print("MENÚ TRABAJADORES")
    print("-----------------------------------")
    print("1. Registrar trabajadores")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    print("-----------------------------------")
    opc = int(input("Ingrese opción: "))
    os.system("cls")

    if opc==1:
        print("Registrar trabajadores")
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = int(input("Ingrese cargo (1: CEO, 2: DESARROLLADOR, 3: ANALISTA): "))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_bruto)
        desc_afp = int(12/100 * sueldo_bruto)
        sueldo_liquido = sueldo_bruto-desc_salud-desc_afp

        trabajador = [nombre_apellido, cargo, sueldo_bruto, desc_salud, desc_afp, sueldo_liquido]
        trabajadores.append(trabajador)
        print("Trabajador registrado con éxito!")

    elif opc==2:
        if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            print("\tLISTA DE TRABAJADORES")
            print("Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. afp\tLiquido a pagar")
            for t in trabajadores: # t: seris cada trabajador de la lista - t es una lista
                print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")
    elif opc==3:
        pass
    else:
        print("gracias por usar el programa, adios!")
        break
    time.sleep(3)