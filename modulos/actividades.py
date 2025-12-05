import csv
import os
ARCHIVO_ACTIVIDADES="datos/actividades.csv"

def listar_actividades():
    
    with open(ARCHIVO_ACTIVIDADES, "r") as archivo:
     reader=csv.reader(archivo)
     for fila in reader:
      print(f"Actividad: {fila[0]}- Horarios:{fila[1]}- Monto mensual:{fila[2]}")