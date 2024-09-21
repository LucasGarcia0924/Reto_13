def mezclardict(dicc1: dict, dicc2: dict): # Se ingresan los dos diccionarios y se mezclan para imprimir el nuevo
    # Se agrega la llave, con su item del dicc2, si esta no hace parte del dicc1
    [dicc1.update({i:dicc2[i]}) for i in dicc2 if (i in dicc1) == False]
    dicc3: dict = dicc1 # dicc3 es igual al dicc1 actualizado
    print(f"El Nuevo diccionario es:\n{dicc3}") # Se imprimen resultados

if __name__ == "__main__": # Función main para iniciar el código 
    # Se declaran e incializan los diccionarios a utilizar como parámetros
    dicc1 : dict = {31:"Arroz", 25:"Cerdo asado", 32:"Tajadas verdes", 77:"Ensalada de papa"}
    dicc2 : dict = {83:"Malteada", 32:"Helado", 55:"Gaseosa", 17:"Pastel", 68:"Dulce", 5:"Mandarina"}

    # Se llama a la función para mezclar los diccionarios e imprimir los resultados
    mezclardict(dicc1, dicc2)