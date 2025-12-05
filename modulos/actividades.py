import csv
import os
ARCHIVO_ACTIVIDADES="datos/actividades.csv"
while True:
    print("\nOpciones:")
    print("1. Ver actividades")
    print("2. Inscribir socio")
    print("3. Ver inscritos en una actividad")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        mostrar_actividades()
    elif opcion == "2":
        actividad = input("Nombre de la actividad: ")
        socio_id = input("ID del socio: ")
        inscribir_socio(actividad, socio_id)
    elif opcion == "3":
        actividad = input("Nombre de la actividad: ")
        ver_inscritos(actividad)
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")


def mostrar_actividades():
    print("\nActividades disponibles:")
    for actividad, (cupo, inscritos) in actividades.items():
        disponibles = cupo - len(inscritos)
        print(f"- {actividad}: Cupo disponible: {disponibles}/{cupo}")

def inscribir_socio(actividad, socio_id):
    if actividad in actividades:
        cupo, inscritos = actividades[actividad]
        if len(inscritos) < cupo:
            if socio_id not in inscritos:
                inscritos.append(socio_id)
                print(f"Socio {socio_id} inscrito en {actividad}.")
            else:
                print(f"Socio {socio_id} ya está inscrito en {actividad}.")
        else:
            print(f"No hay cupo en {actividad}.")
    else:
        print("Actividad no encontrada.")

def ver_inscritos(actividad):
    if actividad in actividades:
        cupo, inscritos = actividades[actividad]
        print(f"Inscritos en {actividad}: {inscritos}")
    else:
        print("Actividad no encontrada.")
              
        