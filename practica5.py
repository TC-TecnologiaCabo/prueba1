# -*- coding: utf-8 -*-
'''
El ejercicio consiste en unir todos los documentos en uno solo
'''
import os

carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"

carpeta_salida="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"

archivo_salida="UNION.txt"

archivos_lista=os.listdir(carpeta_nombre)

union=""
for archivo_nombre in archivos_lista:
	archivo=open(carpeta_nombre+archivo_nombre)
	texto = archivo.read()
	archivo.close()
	union+=texto

with open(carpeta_salida+archivo_salida,"w") as salida:
	salida.write(union)