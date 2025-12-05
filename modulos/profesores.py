import csv
import os

ARCHIVO_PROFESORES="datos/profesores.csv"

def menu_profesores():
    while True:
        print("\n---Gestión de Profesores---")
        print("1. Registrar profesor")
        print("2. Buscar profesor")
        print("3. Listar profesores")
        print("4. Eliminar profesor")
        print("5. Volver")

        opcion= input("Seleccione una opcion: ")

        if opcion== "1":
            registrar_profesor()
        elif opcion=="2":
            buscar_profesor()
        elif opcion=="3":
            listar_profesor()
        elif opcion=="4":
            eliminar_profesor()
        elif opcion=="5":
            break
        else:
            print("Opcion inválida.")


def registrar_profesor():
    nombre=input("Ingrese nombre de profesor: ")
    edad= input("Edad: ")
    telefono=input("Teléfono: ")
    dni=input("DNI: ")
    with open(ARCHIVO_PROFESORES, "a", newline="") as archivo:
        writer=csv.writer(archivo)
        writer.writerow([nombre,edad,telefono,dni])

        print("Profesor registrado correctamente.")


def buscar_profesor():
    nombre=input("Ingrese el nombre del profesor que desea buscar: ").lower()

    with open(ARCHIVO_PROFESORES, "r") as archivo:
        reader=csv.reader(archivo)
        for fila in reader:
            if nombre in fila [0].lower():
                print(f"Encontrado: {fila}")
                return
            print("Profesor no encontrado")

def listar_profesor():
    if not os.path.exists(ARCHIVO_PROFESORES):
        print("No hay profesores registrados aún.")
        return
    
    with open(ARCHIVO_PROFESORES, "r") as archivo:
     reader=csv.reader(archivo)
     for fila in reader:
      print(f"Nombre: {fila[0]}- Edad:{fila[1]}- Teléfono:{fila[2]}, DNI:{fila[3]}")


def eliminar_profesor():
    dni_eliminar=input("Ingrese el DNI del socio que desea eliminar: ")
    profesor_actualizados= []
    encontrados= False
    with open(ARCHIVO_PROFESORES, "r", newline="") as archivo:
        reader= csv.reader(archivo)
        for row in reader:
            if row[3]==dni_eliminar:
                encontrado= True
            else:
                profesor_actualizados.append(row)

    if encontrado:
        with open(ARCHIVO_PROFESORES, "w",newline="") as archivo:
            writer=csv.writer(archivo)
            writer.writerows(profesor_actualizados)
            print("Profesor eliminado correctamente.")
    else:
        print("Profesor no encontrado ")   
                 
menu_profesores()

