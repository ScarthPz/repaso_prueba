import os, time

from funciones import * 


while True:
    os.system("cls")
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
        opcion_1()
    elif opc==2:
        opcion_2
    elif opc==3:
        opcion_3
    else:
       opcion_4()
    time.sleep(3)