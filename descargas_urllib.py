from urllib.request import urlopen, Request
import os





class Descargar():


	def __init__(self, url, nombre):	#direccion web del archivo y el nombre con el que vas a guardar el archivo

		user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

		
		sitio, extencion = os.path.splitext(url)	#tomamos la extencion del archivo


		with open(f"{nombre}{extencion}", "wb") as file:
			peticion = Request(url = url, headers = user_agent)	#hacemos la peticion


			with urlopen(peticion) as respuesta:
				file.write(respuesta.read())	#guardamos el archivo

