# Se importan los módulos necesarios para cargar el contenido de las APIs y mostrar la fecha
import json
import requests
from datetime import datetime

# Se hace la petición a la API de bromas, se imprime el JSON y se entrega el contenido
def broma(urls: list):
    print(f"\n{urls[0]}\n")
    peticion = requests.get(urls[0])
    print(f"{peticion}\n")
    return json.loads(peticion.content)

# Se hace la petición a la API de perros, se imprime el JSON y se entrega el contenido
def perros(urls: list):
    print(f"\n{urls[1]}\n")
    peticion = requests.get(urls[1])
    print(f"{peticion}\n")
    return json.loads(peticion.content)

# Se hace la petición a la API de gatos, se imprime el JSON y se entrega el contenido
def gatos(urls: list):
    print(f"\n{urls[2]}\n")
    peticion = requests.get(urls[2])
    print(f"{peticion}\n")
    return json.loads(peticion.content)

def ImprimirAPIs(urls): # Función madre para llamar a las demás e imprimir resultados
    
    # Obtiene el contenido del JSON de bromas e imprime el conjunto de llaves y valores
    bromita : str = broma(urls)
    print(bromita)
    for k,v in bromita.items():
        print(k, "->", v)
    
    # Obtiene el contenido del JSON de fotos de perros e imprime el conjunto de llaves y valores
    fotoPerro : str = perros(urls)
    print(fotoPerro)
    for k,v in fotoPerro.items(): 
        print(k, "->", v)

    # Obtiene el contenido del JSON de datos de gatos e imprime el conjunto de llaves y valores
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