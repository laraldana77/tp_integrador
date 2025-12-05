from modulos.socios import menu_socios
from modulos.profesores import menu_profesores
from modulos.pagos import menu_pagos

def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE GIMNASIO ===")
        print("1. Gestión de Clientes")
        print("2. Gestión de profesores")
        #print("2. Gestión de Rutinas")
        print("3. Gestión de Pagos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_socios()
        elif opcion == "2":
            menu_profesores()
        elif opcion == "3":
            menu_pagos()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



if __name__ == "_main_":
    menu_principal()
