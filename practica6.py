# -*- coding: utf-8 -*-

'''
El ejercicio consiste en obtener el vocabulario de TODOS los documentos, es decir, cada palabra y simbolo que se usa, dentro de una lista SIN repeticiones
'''

carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="documento2.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
	texto=texto.replace(simbolo," " + simbolo + " ")

palabras_lista=texto.split()

palabras_unicas=[]
for palabra in palabras_lista:
	if palabra in palabras_unicas:
		continue
	palabras_unicas.append(palabra)
print(palabras_unicas)
num=len(palabras_unicas)
print("numero de palabras unicas en el documento:",num)
num2=len(palabras_lista)
print("numero de palabras de todo el documento:",num2)
# EN ESTE PUNTO LA SOLUCIÃ“N ESTÃ EN palabras_unicas