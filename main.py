from modulos.socios import menu_socios
from modulos.profesores import menu_profesores
from modulos.pagos import menu_pagos
from modulos.actividades import menu_actividades

def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE GIMNASIO ===")
        print("1. Clientes")
        print("2. Profesores")
        print("3.Actividades")
        print("4. Pagos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_socios()
        elif opcion == "2":
            menu_profesores()
        elif opcion == "3":
            menu_actividades()
        elif opcion =="4":
            menu_pagos()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



if __name__ == "_main_":
    menu_principal()
