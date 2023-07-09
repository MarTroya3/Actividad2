"""
    Actividad 2 -Programacion Avanzada
"""

import requests
import time
import csv
import threading
#Librería para ejecutar las operaciones en el sistema de archivos.
import os
# librería de python que permite ejecutar comandos
import subprocess

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            num = row[0].split("|")[0] #obtener el numero de link
            url = row[0].split("|")[1] #obtener la url
            # print("Iteracion: ", row," Numero: ", num," Direccion: ", url) 
            #Comprobar el bucle
            # pass
             lista.append([num, url]) #Agrega un nuevo pares elemento al final de la lista.

    #print(lista) #comprobacion de que si esta guardando en list  
    # se retorna la lista con la información que se necesita
    return lista

def worker(num, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    # pass
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(num, url))
    hilo1.start()
