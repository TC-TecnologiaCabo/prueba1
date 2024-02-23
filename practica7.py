# -*- coding: utf-8 -*-

'''
El ejercicio consiste en utilizar el acento circunflejo de expresiÃ³n regular sobre cada lÃ­nea de un texto.
'''

import re

carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="documento2.txt"
# -*- coding: utf-8 -*-

'''
El ejercicio consiste en repetir el ejercicio anterior usando final del texto en lugar de inicio
'''

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

expresion_regular=re.compile(r".$")

for linea in lineas_lista:
	resultado_busqueda=expresion_regular.search(linea)
	if resultado_busqueda:
		print(resultado_busqueda.group(0))