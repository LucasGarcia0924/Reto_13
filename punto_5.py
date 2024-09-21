# Se importan los módulos necesarios para cargar el contenido de las APIs y mostrar la fecha
import json
import requests
from datetime import datetime

# Se hace la petición a la API de bromas y se entrega el contenido
def broma(urls: list):
    print(urls[0])
    peticion = requests.get(urls[0])
    print(peticion)
    return json.loads(peticion.content)

# Se hace la petición a la API de bitcoin y se entrega el contenido
def bitcoinData(urls: list):
    print(urls[1])
    peticion = requests.get(urls[1])
    print(peticion)
    return json.loads(peticion.content)

# Función para hacer la petición a la API del Perfil Falso e imprimir su contenido
def fakeProfile(urls: list):
    
    # Se declaran e inicializan las variables
    listaImprimir: list = []
    perfilFalso : str

    # Se hace la petición y se carga el contenido de la API
    print(f"\n{urls[2]}")
    peticion = requests.get(urls[2])
    print(peticion)
    perfilFalso = json.loads(peticion.content)

    # Se imprimen los datos del usuario
    print(f"\nLos datos de tu nuevo usuario son:\nGénero: {perfilFalso['results'][0]['gender']}")

    # Bucle para imprimir cada parte del nombre en la misma línea sin estar en una lista
    for seccion in perfilFalso['results'][0]['name']:
        listaImprimir.append(perfilFalso['results'][0]['name'][seccion])
    print(f"Nombre completo: {listaImprimir[0]} {listaImprimir[1]} {listaImprimir[2]}")

    # Se obtiene la fecha de nacimiento en la API
    fecha = perfilFalso['results'][0]['dob']['date']
    # Se convierte el string a un objeto datetime
    fecha = datetime.fromisoformat(fecha.replace("Z", "+00:00"))
    # Se formatea la fecha en un formato legible
    fecha = fecha.strftime("%d of %B of %Y, %H:%M:%S")
    # Se imprime el resultado y la edad actual
    print(f"Fecha de Nacimiento: {fecha} Edad: {perfilFalso['results'][0]['dob']['age']} años")

    listaImprimir = [] # Se reinicializa la variable
    for seccion in perfilFalso['results'][0]['location']['street']:
        listaImprimir.append(perfilFalso['results'][0]['location']['street'][seccion])
    print(f"Dirección: {listaImprimir[0]} {listaImprimir[1]}\nUbicación:") # Se imprime los datos de la dirección
    for seccion in perfilFalso['results'][0]['location']:
        # Se imprime la ubicación, omitiendo dirección, coordenadas, zona horario y descripción
        if seccion == 'street' or seccion == 'coordinates' or seccion == 'timezone' or seccion == 'description':
            continue
        print(perfilFalso['results'][0]['location'][seccion])

    # Se obtiene e imprime el email falso
    email = perfilFalso['results'][0]['email']
    print(f"Email: {email}")

    # Se obtienen e imprimen el usuario y contraseña falsos
    user = perfilFalso['results'][0]['login']['username']
    pw = perfilFalso['results'][0]['login']['password']
    print(f"Usuario: {user}")
    print(f"Contraseña: {pw}\n")


def ImprimirAPIs(urls): # Función madre para llamar a las demás e imprimir resultados
    
    # Obtiene la broma e imprime el inicio y el remate por separado
    bromita : str = broma(urls)
    print(f"\nTop 10 mejores bromas del siglo 21:\n{bromita['setup']}\n {bromita['punchline']}\n")
    
    # Obtiene los datos del bitcoin e imprime cuándo se consultaron y la conversión a varias monedas
    bitcoin : str = bitcoinData(urls)
    print(f"\nActualmente: {bitcoin['time']['updated']}, el {bitcoin['chartName']} equivale a:")
    for moneda in bitcoin['bpi']:
        print(f"{moneda}: {bitcoin['bpi'][moneda]['rate']} {bitcoin['bpi'][moneda]['description']}")

    # Se llama a la función del perfil falso donde se imprimen también los resultados
    fakeProfile(urls)


if __name__ == "__main__": # Función main para dar inicio al código

    # Se declaran e inicializan las url
    urlBroma : str = "https://official-joke-api.appspot.com/random_joke"
    urlBitcoin : str = "https://api.coindesk.com/v1/bpi/currentprice.json"
    urlFakeUser : str = "https://randomuser.me/api/"
    urls: list = [urlBroma, urlBitcoin, urlFakeUser] # Se guardan en una lista
    ImprimirAPIs(urls) # Se llama a la función madre