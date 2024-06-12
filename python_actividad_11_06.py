import csv
import json

# Leer el archivo CSV
with open("listadoRutEmpresa.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Obtener los encabezados
    headers.append('clasificacionEmpresa')  # Agregar el nuevo encabezado
    data = list(reader)  # Convertir el reader a una lista

# Clasificar las ventas y agregar la clasificación a los datos
for row in data:
    ventas = int(row[2])  # Las ventas están en la tercera columna
    if ventas < 100000000:
        row.append('Pequeño Contribuyente')
    elif 100000001 <= ventas <= 200000000:
        row.append('Mediano Contribuyente')
    else:
        row.append('Gran Contribuyente')

# Escribir los datos en un archivo JSON
with open("segmentacionEmpresas.json", "w") as json_file:
    json_data = [dict(zip(headers, row)) for row in data]  # Convertir cada fila a un diccionario
    json.dump(json_data, json_file, ensure_ascii=False)