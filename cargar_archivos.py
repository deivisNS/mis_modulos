import os
import re





class Cargar():


	def ir_a_ruta(self, ruta):	#ingresamos la ruta

		os.chdir(ruta)	#vamos a la ruta

		lista = os.listdir(".")	#tomamos todos los archivos y carpetas


		archivos = []


		for archivo in lista:

			if re.findall(".mp3$", cancion):	#guardamos los archivos que queremos dependiendo de sus extencion
				archivos.append(archivo)


		return archivos

