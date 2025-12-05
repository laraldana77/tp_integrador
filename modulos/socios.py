import csv
import os

ARCHIVO_SOCIOS="datos/socios.csv"

def menu_clientes():
    while True:
        print("\n---Gestión de Socios---")
        print("1. Registrar socio")
        print("2. Buscar socio")
        print("3. Listar socios")
        print("4. Eliminar socio")
        print("5. Volver")

        opcion= input("Seleccione una opcion: ")

        if opcion== "1":
            registrar_socio()
        elif opcion=="2":
            buscar_socio()
        elif opcion=="3":
            listar_socios()
        elif opcion=="4":
            eliminar_socio()
        elif opcion=="5":
            break
        else:
            print("Opcion inválida.")


def registrar_socio():
    nombre=input("Ingrese nombre de socio: ")
    edad= input("Edad: ")
    telefono=input("Teléfono: ")
    dni=input("DNI: ")
    with open(ARCHIVO_SOCIOS, "a", newline="") as archivo:
        writer=csv.writer(archivo)
        writer.writerow([nombre,edad,telefono,dni])

        print("Cliente registrado correctamente.")


def buscar_socio():
    nombre=input("Ingrese el nombre del socio que desea buscar: ").lower()

    with open(ARCHIVO_SOCIOS, "r") as archivo:
        reader=csv.reader(archivo)
        for fila in reader:
            if nombre in fila [0].lower():
                print(f"Encontrado: {fila}")
                return
            print("Socio no encontrado")

def listar_socios():
    if not os.path.exists(ARCHIVO_SOCIOS):
        print("No hay socios registrados aún.")
        return
    
    with open(ARCHIVO_SOCIOS, "r") as archivo:
     reader=csv.reader(archivo)
     for fila in reader:
      print(f"Nombre: {fila[0]}- Edad:{fila[1]}- Teléfono:{fila[2]}, DNI:{fila[3]}")


def eliminar_socio():
    dni_eliminar=input("Ingrese el DNI del socio que desea eliminar: ")
    socios_actualizados= []
    encontrados= False
    with open(ARCHIVO_SOCIOS, "r", newline="") as archivo:
        reader= csv.reader(archivo)
        for row in reader:
            if row[3]==dni_eliminar:
                encontrado= True
            else:
                socios_actualizados.append(row)

    if encontrado:
        with open(ARCHIVO_SOCIOS, "w",newline="") as archivo:
            writer=csv.writer(archivo)
            writer.writerows(socios_actualizados)
            print("Socio eliminado correctamente.")
    else:
        print("Socio no encontrado ")            
menu_clientes()
