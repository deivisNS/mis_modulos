import mutagen
import os





class Datos_Musical():

	nombre_cancion = ""


	datos = {}





	def datos_cancion(self, nombre):	#nombre de la cancion (debe de estar junto al ejecutable)

		self.cancion = mutagen.File(nombre)	#analiza la cancion


		self.datos = {}


		nombre_cancion, extencion = os.path.splitext(nombre)	#dividimos el nombre y la extencion

		self.datos["nombre cancion"] = nombre_cancion	#guardamos el nombre

		self.datos["extencion"] = extencion	#guardamos la extencion
		
		
		longitud = self.cancion.info.length	#pedimos la duracion de la cancion (es devuelto en milisegundos)

		minutos, segundos = divmod(longitud, 60)	#dividimos la duracion de la cancion para que nos devuelva los minutos y segundos que dura


		self.datos["longitud de la cancion"] = int(longitud)	#guardamos la duracion 

		self.datos["minutos de la cancion"] = int(minutos)	#guardamos los minutos

		self.datos["segundos de la cancion"] = int(segundos)	#guardamos los segundos


		ruta_cancion = os.getcwd()	#obtenemos la ruta donde se encuentra

		self.datos["ruta de la cancion"] = ruta_cancion	#guardamos la ruta


		tamanno = os.path.getsize(nombre)	#obtenemos el peso de la cancion en bytes

		self.datos["tamaño de la cancion"] = f"{tamanno} bytes"	#guardamos el peso


		return self.datos







