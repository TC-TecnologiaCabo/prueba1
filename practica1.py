carpeta_nombre="C:\\Users\\USUARIO\\Documents\\FIME FEB-JUN 2024\\PLN\\programas-phyton\\"
#"D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="acuerdo.txt"

palabra1="Acuerdo"
palabra2="RESOLUCIÃ“N"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()
	
if palabra1 in texto:
	print("El documento es un(a)",palabra1)
	
elif palabra2 in texto:
	print("El documento es un(a)",palabra2)
	
else:
	print("El documento no es ni un ACUERDO ni una RESOLUCIÃ“N")