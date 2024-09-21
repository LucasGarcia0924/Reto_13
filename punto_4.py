# Se importan los módulos necesarios para cargar el json y obtener la fecha de las alertas
import json
from datetime import datetime, timezone

# Función para cargar el contnenido del json a un string
def CargarJson():
    jsonString = '''
    {\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
    '''
    return json.loads(jsonString)

# Función que entrega la fecha en formato cada vez que sea llamada
def Obtenerfecha(data: str, dia: str):
    fechaNum: str = data['dt'][dia]
    return datetime.fromtimestamp(fechaNum, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

# Función para verificar si hay alertas de alertas
def AnalisisAlertas(data: str):
    print("\nEn cuanto a alertas generales:\n")

    # En teoría aquí se llamaría a otras funciones para buscar alertas, pero el pronóstico no muestra ninguna alerta de alertas
    for dia in data['alertAlertas']:
        if data['alertAlertas'][dia] == 'X':
            print(f"Hay alerta en el día {dia}:")
        else:
            print(f"En el día {dia} no hay alerta")

# Función para verificar si hay alertas de precipitación
def AnalisisPrecip(data: str): 
    print("\nEn cuanto a alertas de precipitación:\n")
    for dia in data['alertPrecip']:

        # Si hay una alerta se llama a la función que muestra las variables asociadas
        if data['alertPrecip'][dia] == 'X':
            print(f"Hay alerta en el día {dia}:")
            AlertaPrecip(data, dia)
        else:
            print(f"En el día {dia} no hay alerta") # Sino, se reporta que no hay alertas

# Función encargada de mostrar los datos asociados a las precipitaciones cuando hay una alerta
def AlertaPrecip(data: str, dia: str):

    # Se declaran e inicializan las variables
    fecha: str = Obtenerfecha(data, dia)
    presion: str = data['pressure'][dia]
    humedad: str = data['humidity'][dia]
    puntoRocio: str = data['dew_point'][dia]
    descripcion: str = data['weather'][dia][0]['description']
    nubes: str = data['clouds'][dia]
    probPrecip = (float(data['pop'][dia]))*100
    precip: str = data['prcp'][dia]

    # Se imprimen los resultados en un formato
    print(f"A la fecha del {fecha}")
    print(f"la presión atmosférica será de {presion} Milibares")
    print(f"la humedad será del {humedad}%")
    print(f"el punto de rocío será de {puntoRocio} grados celcius")
    print(f"se espera un clima de {descripcion}")
    print(f"el cielo se encontrará cubierto en un {nubes}% por nubes")
    print(f"habrá una probabilidad del {probPrecip}% de precipitación")
    print(f"se espera una lluvia de {precip} milímetros.\n")

# Función para verificar si hay alertas por temperatura máxima
def AnalisisTmpMax(data: str):
    print("\nEn cuanto a alertas de temperatura máxima:\n")
    for dia in data['alertTmpMax']:

        # Si hay una alerta se llama a la función que muestra las variables asociadas
        if data['alertTmpMax'][dia] == 'X':
            print(f"\nHay alerta en el día {dia}:")
            AlertaTmpMax(data, dia)
        else:
            print(f"En el día {dia} no hay alerta") # Sino, se reporta que no hay alertas

# Función encargada de mostrar los datos asociados a la temperatura máxima cuando hay una alerta
def AlertaTmpMax(data: str, dia: str):
    
    # Se declaran e inicializan las variables
    fecha: str = Obtenerfecha(data, dia)
    humedad: str = data['humidity'][dia]
    puntoRocio: str = data['dew_point'][dia]
    TmpProm: str = data['temp.day'][dia]
    TmpMax: str = data['tmpMax'][dia]
    TmpNoche: str = data['temp.night'][dia]
    TmpTarde: str = data['temp.eve'][dia]
    TmpMorn: str = data['temp.morn'][dia]
    SensProm: str = data['feels_like.day'][dia]
    SensNoche: str = data['feels_like.night'][dia]
    SensTarde: str = data['feels_like.eve'][dia]
    SensMorn: str = data['feels_like.morn'][dia]

    # Se imprimen los resultados en un formato
    print(f"A la fecha de {fecha}")
    print(f"la humedad será del {humedad}%")
    print(f"el punto de rocío será de {puntoRocio} grados celcius")
    print(f"se espera una temperatura máxima de {TmpMax} grados celcius")
    print(f"\nse espera una temperatura de {TmpProm} grados celcius en el día")
    print(f"se espera una temperatura de {TmpNoche} grados celcius en la noche")
    print(f"se espera una temperatura de {TmpTarde} grados celcius en la tarde")
    print(f"se espera una temperatura de {TmpMorn} grados celcius en la mañana\n")
    print(f"se espera una sensación térmica de {SensProm} grados celcius en el día")
    print(f"se espera una sensación térmica de {SensNoche} grados celcius en la noche")
    print(f"se espera una sensación térmica de {SensTarde} grados celcius en la tarde")
    print(f"se espera una sensación térmica de {SensMorn} grados celcius en la mañana.\n")

# Función para verificar si hay alertas por temperatura mínima
def AnalisisTmpMin(data: str):
    print("\nEn cuanto a alertas de temperatura mínima:\n")
    for dia in data['alertTmpMin']:

        # Si hay una alerta se llama a la función que muestra las variables asociadas
        if data['alertTmpMin'][dia] == 'X':
            print(f"\nHay alerta en el día {dia}:")
            AlertaTmpMin(data, dia)
        else:
            print(f"En el día {dia} no hay alerta") # Sino, se reporta que no hay alertas

# Función encargada de mostrar los datos asociados a la temperatura mínima cuando hay una alerta
def AlertaTmpMin(data: str, dia: str):
    
    # Se declaran e inicializan las variables
    fecha: str = Obtenerfecha(data, dia)
    humedad: str = data['humidity'][dia]
    puntoRocio: str = data['dew_point'][dia]
    TmpProm: str = data['temp.day'][dia]
    TmpMin: str = data['tmpMin'][dia]
    TmpNoche: str = data['temp.night'][dia]
    TmpTarde: str = data['temp.eve'][dia]
    TmpMorn: str = data['temp.morn'][dia]
    SensProm: str = data['feels_like.day'][dia]
    SensNoche: str = data['feels_like.night'][dia]
    SensTarde: str = data['feels_like.eve'][dia]
    SensMorn: str = data['feels_like.morn'][dia]

    # Se imprimen los resultados en un formato
    print(f"A la fecha del {fecha}")
    print(f"la humedad será del {humedad}%")
    print(f"el punto de rocío será de {puntoRocio} grados celcius")
    print(f"se espera una temperatura mínima de {TmpMin} grados celcius")
    print(f"\nse espera una temperatura de {TmpProm} grados celcius en el día")
    print(f"se espera una temperatura de {TmpNoche} grados celcius en la noche")
    print(f"se espera una temperatura de {TmpTarde} grados celcius en la tarde")
    print(f"se espera una temperatura de {TmpMorn} grados celcius en la mañana\n")
    print(f"se espera una sensación térmica de {SensProm} grados celcius en el día")
    print(f"se espera una sensación térmica de {SensNoche} grados celcius en la noche")
    print(f"se espera una sensación térmica de {SensTarde} grados celcius en la tarde")
    print(f"se espera una sensación térmica de {SensMorn} grados celcius en la mañana.\n")

# Función para verificar si hay alertas por velocidad del viento
def AnalisisVelViento(data: str):
    print("\nEn cuanto a alertas de velocidad del viento:\n")
    for dia in data['alertVelViento']:
        
        # Si hay una alerta se llama a la función que muestra las variables asociadas
        if data['alertVelViento'][dia] == 'X':
            print(f"\nHay alerta en el día {dia}:")
            AlertaVelViento(data, dia)
        else:
            print(f"En el día {dia} no hay alerta") # Sino, se reporta que no hay alertas

# Función encargada de mostrar los datos asociados al viento cuando hay una alerta
def AlertaVelViento(data: str, dia: str):
    
    # Se declaran e inicializan las variables
    desde: str
    hasta: str
    fecha: str = Obtenerfecha(data, dia)
    presion: str = data['pressure'][dia]
    velViento: str = data['velViento'][dia]
    rafagasVient: str = data['wind_gust'][dia]
    
    # Se obtiene la dirección del viento y con match-case se determina desde y hacia donde se dirige
    dirViento = int(data['dirViento'][dia])
    if dirViento == 0:
        desde = 'norte'
        hasta = 'sur'
    elif dirViento > 0 and dirViento < 90:
        desde = 'noreste'
        hasta = 'suroeste'
    elif dirViento == 90:
        desde = 'este'
        hasta = 'oeste'
    elif dirViento > 90 and dirViento < 180:
        desde = 'sureste'
        hasta = 'noroeste'
    elif dirViento == 180:
        desde = 'sur'
        hasta = 'norte'
    elif dirViento > 180 and dirViento < 270:
        desde = 'suroeste'
        hasta = 'noreste'
    elif dirViento == 270:
        desde = 'oeste'
        hasta = 'este'
    else:
        desde = 'noroeste'
        hasta = 'sureste'

    # Se imprimen los resultados en un formato
    print(f"A la fecha del {fecha}")
    print(f"la presión atmosférica será de {presion} Milibares")
    print(f"la velocidad del viento será de {velViento} m/s")
    print(f"con ráfagas de {rafagasVient} m/s")
    print(f"y el viento vendrá con {dirViento} grados desde el {desde} hasta el {hasta}.\n")

# Función principal encargada de llamar a todas las demás funciones
def AnalisisGeneral():
    data: str = CargarJson()
    AnalisisAlertas(data)
    AnalisisPrecip(data)
    AnalisisTmpMax(data)
    AnalisisTmpMin(data)
    AnalisisVelViento(data)

if __name__ == "__main__": # Función main para iniciar el código
    AnalisisGeneral() # Se llama a la función principal