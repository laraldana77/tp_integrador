import csv
import os

ARCHIVO_ACTIVIDADES = "datos/actividades.csv"

def menu_actividades():
    while True:
        print("\n--- Menu de Actividades ---")
        print("1. Listar actividades")
        print("2. Inscripción socios")
        print("3. Volver")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
           listar_actividades()
       
        elif opcion == "2":
            socio = input("Nombre del socio: ")
            actividad = input("Actividad a inscribir: ")
            inscribir_socio(socio, actividad)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")




def listar_actividades():
    if not os.path.exists(ARCHIVO_ACTIVIDADES):
        print("No hay actividades registradas aún.")
        return
     
    with open(ARCHIVO_ACTIVIDADES, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)

        print("\n=== ACTIVIDADES DISPONIBLES ===")

        next(reader, None)  # <-- SALTA EL ENCABEZADO

        for fila in reader:
            print(f"Actividad: {fila[0]} | Horario: {fila[1]} | Costo: {fila[2]}")


archivo_inscripciones = "inscripciones.csv"

def inscribir_socio(socio, actividad):
    existe = os.path.exists(archivo_inscripciones)

    with open(archivo_inscripciones, "a", newline="", encoding="utf-8") as f:
        campos = ["socio", "actividad"]
        escritor = csv.DictWriter(f, fieldnames=campos)

        if not existe:
            escritor.writeheader()

        escritor.writerow({
            "socio": socio,
            "actividad": actividad
        })

    print(f"\n✔ El socio '{socio}' fue inscripto a '{actividad}'.\n")

