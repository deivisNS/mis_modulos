"""hago app de escritorio y a veces necesito usar scrollbar, pero hay momentos donde no me funcionaba,
asi que decidi hacer este modulo que divide contenido como si fueran paginas a pasar"""



class Dividir():

	partes = {}
	contenedor = []


	progreso = 0
	pagina = 1





	def construir_partes(self, por_cada, contenido):

		for I in contenido:	              #recorre listas o textos

			self.contenedor.append(I)


			self.progreso += 1


			if self.progreso == por_cada:

				self.partes[str(self.pagina)] = self.contenedor		#crea la pagina con la cantidad deseada


				self.progreso = 0
				self.pagina += 1


				self.contenedor = []


		if self.contenedor:
			self.partes[str(self.pagina)] = self.contenedor


		return self.partes                 	#devuelve un diccionario con los datos se parados



#EJEMPLO

D = Dividir()

				# 1. cada pagina tendra 3 datos || 2. lista a separar en paginas
print(D.construir_partes(3, ["ronaldo", "joselu", "rodrygo", "kroos", "modric", "benzema", "kepa"]))  