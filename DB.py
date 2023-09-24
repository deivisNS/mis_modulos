import sqlite3
import os





class DB():

	resultado = []





	def crear_DB(self):

		self.conexion = sqlite3.connect("DB/Datos Registrados.db")	#conectar a la base de datos
		self.puntero = self.conexion.cursor()	#crear cursor


		try:
			self.puntero.execute("""CREATE TABLE nombre_db (id integer)""")	#crear tabla con sus campos


		except:
			pass





	def comprobar_creacion(self):	#comprueba si existe la base de datos

		if os.path.exists("DB/Datos Registrados.db"):
			return True


		else:
			return False





	def ingresar_datos(self, opcion):
		
		self.puntero.execute(f"INSERT INTO nombre_db VALUES ({opcion})")	#ingresar dato en su campo correspondiente
		

		self.cerrar_db()





	def imprimir_datos(self):

		self.puntero.execute("SELECT * FROM nombre_db")		#extrae la informacion de la base de datos
		self.resultado = self.puntero.fetchall()


		self.cerrar_db()





	def actualizar_datos(self, tabla, actualizar, opcion):
		
		self.puntero.execute(f"UPDATE nombre_db SET {tabla} = '{actualizar}' WHERE id = {opcion}")	#actualiza una informacion de algun campo


		self.cerrar_db()





	def eliminar_datos(self, tabla, valor):
		
		self.puntero.execute(f"DELETE FROM {tabla} WHERE {tabla} = '{valor}'")  #elimina informacion de algun campo 


		self.cerrar_db()





	def cerrar_db(self):	#procesa y cierra la base de datos
		
		self.conexion.commit()
		self.conexion.close()
