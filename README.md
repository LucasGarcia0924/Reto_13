# Reto_13
Descripción de cómo fueron solucionados todos los incisos de dicho reto.
## Inciso 1
Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
***
Para esto decidí crear un programa que al ingresar individuos, registre sus edades y estos dos valores queden asociados en un diccionario.
```python 
def CrearDicc(Bandera : bool): # Función para crear el diccionario
    edades: dict = {} # Se crea la variable del diccionario vacio
    # Se imprimen instrucciones
    print("Hagamos una lista de personas con sus edades")
    print("Cuando ya no vaya a agregar más individuos presione ENTER")
    while Bandera == True: # Bucle para agregar datos al diccionario
        Nombre = str(input("Agrega el nombre de la persona"))
        if Nombre == "":
            break
        print(f"\nNombre: {Nombre}") # Se imprime el nombre en cada iteración
        Edad = int(input("Y ahora su edad"))
        print(f"Edad: {Edad}") # Se imprime la edad en cada iteración 
        edades[Nombre] = Edad # Se agregan los datos al diccionario
    return edades # Se retornan las edades
```
De ahí, en otra función separé las edades de los nombres, las ordené de menor a mayor e imprimí el resultado.
```python
def MostrarValoresAscendentes(Bandera: bool): # Función principal
    valores: list = [] # Se crea la lista vacia de valores para ordenar
    edades = CrearDicc(Bandera) # Se llama a la función para crear el diccionario de edades
    
    # Se crea bucle para tomar los valores y añadir a la lista
    for llav, valor in edades.items():
        valores.append(valor)
    
    valores.sort() # Se orden ascendentemente los valores
    print(f"\nLas edades en orden ascedente son:{valores}") # Se imprimen los valores 
```
## Inciso 2
Desarrollar una función que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
***
Simplemente tomé dos diccionarios y actualizé el primero con los elementos del segundo, a menos de que haya una llave repetida, en cuyo caso el condicional no se cumple y por ende ese valor no se actualiza en el primer diccionario.
```python
def mezclardict(dicc1: dict, dicc2: dict): # Se ingresan los dos diccionarios y se mezclan para imprimir el nuevo
    # Se agrega la llave, con su item del dicc2, si esta no hace parte del dicc1
    [dicc1.update({i:dicc2[i]}) for i in dicc2 if (i in dicc1) == False]
    dicc3: dict = dicc1 # dicc3 es igual al dicc1 actualizado
    print(f"El Nuevo diccionario es:\n{dicc3}") # Se imprimen resultados
```
## Inciso 3
Dado el JSON:
```JSON
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Daz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
Cree un programa que lea de un archivo con dicho JSON e:
- Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
- Imprima los nombres completos (nombre y apellidos) de las personas que estén en un rango de edades dado por el usuario.
***
Primero, guardé el JSON en un archivo el cual se adjuntó con los demás incisos en este repositorio.

Luego realizé una función que se encarga de cargar el contenido del JSON y guardarlo en una variable.
```python
import json # Se importa el módulo json

def CargarArchivo(): # Función para leer el contenido del json
    # Cargar archivo
    readFile = open("punto_3_json.json", "r")
    data = json.load(readFile) # Se guarda el contenido en la variable "data"
    readFile.close()
    return data # Se retorna la variable
```
Posteriormente, construí funciones para ingresar el deporte preferido y el intervalo de edad deseado por el usuario
```python
def elegirdeporte(InterfazDeportes: bool)-> str: # Función para seleccionar un deporte
    print("Elige un deporte para observar cuáles personas lo practican")
    print(InterfazDeportes)
    eleccionDeporte = int(input("Selecciona un número"))
    
    # Estructura Match-Case según cada deporte
    match eleccionDeporte:
        case 1: 
            return "Futbol"
        case 2:
            return "Ajedrez"
        case 3:
            return "Baloncesto"
        case 4:
            return "Gimnasia"
        case _: # En caso de ingresar otro valor se retorna a la misma función
            print("Por favor ingrese una opción válida\n")
            return elegirdeporte()
        
def edadMinima()-> int: # Función para ingresar la edad mínima del intervalo
    while True:
        try:
            edadMin = int(input("Ingresa la edad mínima"))
            return edadMin
        except ValueError: # Se reitera el bucle si el valor no es válido
            print("Ingresa un valor válido\n")
    
def edadMaxima()-> int: # Función para ingresar la edad máxima del intervalo
    while True:
        try:
            edadMax = int(input("Ingresa la edad máxima"))
            return edadMax
        except ValueError: # Se reitera el bucle si el valor no es válido
            print("Ingresa un valor válido\n")
```
Finalmente, se hace un zondeo en los datos del archivo, y si la persona practique ese deporte o tiene una edad en el intervalo dado, se imprime su nombre.

Para esto se llaman a las funciones anteriores y se indexa el diccionario para encontrar la información requerida
```python
def MostrarPreferencias(InterfazDeportes: str): # Función principal donde se ejecutan las demás
    presente: bool = False # Bandera para imprimir mensaje por si no se cumplen las condiciones
    
    # Se llaman a las funciones para cargar el json y para elegir el deporte
    data = CargarArchivo() 
    deporte = elegirdeporte(InterfazDeportes) 
    
    print("Las personas que practican ese deporte son:")
    # Para cada persona listada en el json
    for persona in data.values():
        if deporte in persona["deportes"]: # Si el deporte elegido se encuentra en los que practica...
            print(f"{persona["nombres"]} {persona["apellidos"]}") # Se imprime su nombre completo
            presente = True # Se cambia la bandera para no imprimir el mensaje siguiente

    if not presente: # Si la bandera no recibe cambios se imprime esto:
        print("No se encontraron personas que practiquen este deporte")

    print("\nIngresa un intervalo de edad para mostrar a las personas que pertenezcan a él\n")
    
    # Se llaman a las funciones para ingresar el intervalo
    edadMin = edadMinima()
    edadMax = edadMaxima()
    if edadMin > edadMax: # Si la edad mínima es mayor a la máxima se invierten
        edadMin, edadMax = edadMax, edadMin

    presente = False # Se reinicializa la bandera
    print(f"Las personas con edades de entre {edadMin} y {edadMax} años son:")
    
    # Para cada persona listada en el json
    for persona in data.values():
        # Si la persona tiene una edad dentro del intervalo dado se imprime su nombre completo
        if (persona["edad"]>= edadMin and persona["edad"] <= edadMax):
            print(f"{persona["nombres"]} {persona["apellidos"]}")
            presente = True # Se cambia la bandera para no imprimir el mensaje siguiente

    if not presente: # Si la bandera no recibe cambios se imprime esto:
        print("No se encontraron personas que practiquen entre estas edades")
    

if __name__ == "__main__": # Función main para iniciar el código
    # Se declara la variable que contiene la interfaz de deportes a escoger por el usuario
    InterfazDeportes : str = """
                    Seleccione un número:
    Fútbol (1), Ajedrez (2), Baloncesto (3), Gimnasia (4)
    """
    # Se llama a la función principal
    MostrarPreferencias(InterfazDeportes)
```
# Inciso 4
El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:
```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```
Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt', así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busque el nivel de lluvia, si es vientos, la velocidad del viento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.
***
Para realizar esta tarea, desde la función main se llama a la función "Madre", encargada de llamar a las demás.
```python
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
```
Es desde ahí que se ejecuta para cada alerta un mismo protocolo, buscar en el pronóstico si se encuentra una "X" en cualquier día en el campo de esa alerta, para eso se itera en la alerta y se revisa día por día, ejemplo de esto es la función de análisis de precipitaciones:
```python
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
```
En caso de que lo haga, se llama a la función de alerta correspondiente, en este caso de precipitación y se obtienen los valores asocidados con el fenómeno, así como su fecha, para reportarlos al usuario.
```python
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

# Función que entrega la fecha en formato cada vez que sea llamada
def Obtenerfecha(data: str, dia: str):
    fechaNum: str = data['dt'][dia]
    return datetime.fromtimestamp(fechaNum, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
```
Todo este proceso se repite con las demás alertas presentes en el pronóstico (alertas, temperatura mínima, temperatura máxima y velocidad de vientos), puede observar en el archivo adjunto ["punto_4.py"](https://github.com/LucasGarcia0924/Reto_13/blob/main/punto_4.py) cómo sucede esto en cada una.
# Inciso 5
A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
***
Fue bastante sencillo, únicamente hice la petición a las 3 API's e imprimí además del url, la respuesta que este entrega al hacer la solicitud.
```python
# Se importan los módulos necesarios para cargar el contenido de las APIs y mostrar la fecha
import json
import requests

# Se hace la petición a la API de bromas, se imprime su url y la respuesta que entrega, luego entrega el contenido
def broma(urls: list):
    print(f"\n{urls[0]}\n")
    peticion = requests.get(urls[0])
    print(f"{peticion}\n")
    return json.loads(peticion.content)

# Se hace la petición a la API de perros, se imprime su url y la respuesta que entrega, luego entrega el contenido
def perros(urls: list):
    print(f"\n{urls[1]}\n")
    peticion = requests.get(urls[1])
    print(f"{peticion}\n")
    return json.loads(peticion.content)

# Se hace la petición a la API de gatos, se imprime su url y la respuesta que entrega, luego entrega el contenido
def gatos(urls: list):
    print(f"\n{urls[2]}\n")
    peticion = requests.get(urls[2])
    print(f"{peticion}\n")
    return json.loads(peticion.content)
```
Luego en la función main llamé a la función "Madre" donde se ejecutan las demás y se imprimen los pares llave-valor para cada JSON.
```python
def ImprimirAPIs(urls): # Función madre para llamar a las demás e imprimir resultados
    
    # Obtiene el contenido del JSON de bromas y se imprime junto al conjunto de llaves y valores
    bromita : str = broma(urls)
    print(bromita)
    for k,v in bromita.items():
        print(k, "->", v)
    
    # Obtiene el contenido del JSON de fotos de perros y se imprime junto al conjunto de llaves y valores
    fotoPerro : str = perros(urls)
    print(fotoPerro)
    for k,v in fotoPerro.items(): 
        print(k, "->", v)

    # Obtiene el contenido del JSON de datos de gatos y se imprime junto al conjunto de llaves y valores
    datosGatos : str = gatos(urls)
    print(datosGatos)
    for k,v in datosGatos.items(): 
        print(k, "->", v)

if __name__ == "__main__": # Función main para dar inicio al código

    # Se declaran e inicializan las url
    urlBroma : str = "https://official-joke-api.appspot.com/random_joke"
    urlPerros : str = "https://dog.ceo/api/breeds/image/random"
    urlGatos : str = "https://catfact.ninja/fact"
    urls: list = [urlBroma, urlPerros, urlGatos] # Se guardan en una lista
    ImprimirAPIs(urls) # Se llama a la función madre
```
