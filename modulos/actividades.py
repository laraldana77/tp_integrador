import csv
import os
ARCHIVO_ACTIVIDADES="datos/actividades.csv"
def menu_actividades():
   while True:
      print("\n---Menu de Actividades---")
      print("1. Cargar actividades")
      print("2. Listar actividades")
      print("3. Inscripcion socios")
      print("4. Volver")

      opcion = input("Seleccione opción: ")

      if opcion == "1":
        cargar_actividades()
      elif opcion == "2":
         actividades=cargar_actividades()
         mostrar_actividades()
      elif opcion=="3":
          actividades = cargar_actividades()
          socio = input("Nombre del socio: ")
          actividad = input("Actividad a inscribir: ")
          inscribir_socio(socio, actividad)
      elif opcion=="4":
            break
      else:
            print("Opcion inválida.")


archivo="inscripciones.csv"
def cargar_actividades(archivo="actividades.csv"):
    actividades = []
    if os.path.exists(archivo):
        with open(archivo, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                actividades.append(fila)
    return actividades


def mostrar_actividades():
    with open("ARCHIVO_ACTIVIDADES", "r") as archivo:
        lector = csv.reader(archivo)
        print("=== ACTIVIDADES DISPONIBLES ===")
        for fila in lector:
            actividad = fila[0]
            horario = fila[1]
            costo = fila[2]
            print(f"Actividad: {actividad} | Horario: {horario} | Costo: {costo}")


def inscribir_socio(socio, actividad):
    existe = os.path.exists(archivo)

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        campos = ["socio", "actividad"]
        escritor = csv.DictWriter(f, fieldnames=campos)

        if not existe:
            escritor.writeheader()

        escritor.writerow({
            "socio": socio,
            "actividad": actividad
        })

    print(f"\n✔ El socio '{socio}' fue inscripto a '{actividad}'.\n")

