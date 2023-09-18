import re




class Comprobacion():

	resultado = []

	numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

	caracteres_especiales = ["!", "|", "'", '"', "@", "#", "$", "~", "%", "€",
							"&", "¬", "/", ")", "(", "=", "?", "¿", "¡", "*", "+", "]",
							"`", "^", "[", "´", "¨", "{", "}", "Ç", "ç", "-", "_", ".",
							":", ",", ";", ">", "<", "ª", "º"]

	



	def comprobar_texto(self, texto):	#se puede invocar. analiza un str o lista con solo str dentro, para saber si contiene numeros o caracteres especiales 

		if list(texto):
			self.comprobar_lista_texto(texto)


			if False in self.resultado:
				return False	#devuelve False si en la lista algun elemento no cumple la condicion de ser solo str


			else:
				return True		#devuelve True si en los elementos de la lista niguno lleva numeros o caracteres especiales


		else:


			for numero in self.numeros:


				if re.search(numero, texto):		#busca si hay numeros en el str
					return False


			for t in texto:


				for C_E in self.caracteres_especiales:


					if t == C_E:		#busca si hay caracteres especiales en el str
						return False			


			return True





	def comprobar_lista_texto(self, lista):		#no es necesario invocar, funcion llamada si en la anterior se le ha pasado una lista

		self.resultado = []

		
		for texto in lista:


			for numero in self.numeros:


				if re.search(numero, texto):	#busca numeros en los elementos de las listas
					self.resultado.append(False)


			for text in texto:


				for C_E in self.caracteres_especiales:


					if text == C_E:		#busca caracteres especiales en los elementos de la lista
						self.resultado.append(False)





	def comprobar_numeros(self, numero):	#se puede invocar, analiza un numero o lista con numeros, para saber si solo contiene numeros
		
		try:

			if list(numero):
				self.comprobar_lista_numeros(numero)


				if False in self.resultado:
					return False	#devuelve False si algun elemento de la lista no es solo numerico


				else:
					return True		#devuelve True si los elementos de la lista son solo numericos


		except:

			try:

				if float(numero):	#comprueba si es solo numerico
					return True
					

			except:
				return False





	def comprobar_lista_numeros(self, lista):	#no es necesario invocar, funcion llamada si en la anterior se le a pasado una lista

		self.resultado = []


		for numero in lista:


			try:
			
				if float(numero):	#comprueba si es solo numerico
					self.resultado.append(True)


			except:
				self.resultado.append(False)





#EJEMPLOS:
C = Comprobacion()		

print(C.comprobar_texto("hola amigo"))	#str valido

print(C.comprobar_texto("h0la - amigo"))	#str invalido

print(C.comprobar_texto(["soy", "progamador"]))	 #lista valida

print(C.comprobar_texto(["s0y", "prog@mador"]))	 #lista invalida


print(C.comprobar_numeros(12))	#int valido

print(C.comprobar_numeros("12j"))	#int invalido

print(C.comprobar_numeros([12, "12", "39"]))	#lista valida

print(C.comprobar_numeros([12, "12dd", "39f"]))	  #lista invalida
