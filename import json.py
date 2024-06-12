import json
import csv

data = {}  # Define the variable "data"

with open("Data/listadoRutEmpresa.csv","r",newline='') as listadoRutEmpresa_csv:
    lector_csv = csv.reader(listadoRutEmpresa_csv)

    with open("Data/segmentacionEmpresas.json","w") as segmentacionEmpresas_json:
        json.dump(data, segmentacionEmpresas_json)

    with open("Data/segmentacionEmpresas.json","r") as segmentacionEmpresas_json:
        archivo_lectura = json.load(segmentacionEmpresas_json)
        print(archivo_lectura)



# Definir la función de clasificación
def clasificar(ventas):
    if ventas < 100000000:
        return 'Pequeño Contribuyente'
    elif 100000001 <= ventas <= 200000000:
        return 'Mediano Contribuyente'
    else:
        return 'Gran Contribuyente'

