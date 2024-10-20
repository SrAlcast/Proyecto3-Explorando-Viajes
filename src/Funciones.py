from datetime import datetime, timedelta

def crear_lista_fechas(fecha_inicial, fecha_final):
    # Convertir las cadenas de texto en objetos datetime
    fecha_inicial_dt = datetime.strptime(fecha_inicial, '%Y-%m-%d')
    fecha_final_dt = datetime.strptime(fecha_final, '%Y-%m-%d')
    # Crear una lista con el rango de fechas
    lista_fechas = []
    while fecha_inicial_dt <= fecha_final_dt:
        lista_fechas.append(fecha_inicial_dt.strftime('%Y-%m-%d'))
        fecha_inicial_dt += timedelta(days=1)
    if not lista_fechas:
        return print("La fecha final no puede ser previa a la inicial")
    return lista_fechas

import re
def convertir_duracion_a_minutos(duracion):
    # Ejemplo de formato ISO 8601: "PT2H30M" (2 horas y 30 minutos)
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?', duracion)
    if not match:
        return None
    horas = int(match.group(1)) if match.group(1) else 0
    minutos = int(match.group(2)) if match.group(2) else 0
    return horas * 60 + minutos  # Convertir todo a minutos