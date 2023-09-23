import yagmail





class Correo_Yagmail():

	usuario = "-----------@gmail.com"	#tu correo de gmail
	contrasenna = "------------------"	 #contraseña de aplicaciones gmail


	conexion = yagmail.SMTP(user = usuario, password = contrasenna)	 #nos conectamos con gmail





	def enviar(self, destino, asunto, mensaje, archivo):

		if archivo != "":

			try:
				
				self.conexion.send(destino, asunto, mensaje, attachments = archivo)	 #enviamos el mensaje
				"""(attachments es para enviar algun archivo y se puede enviar varios archivos si colocas
				las rutas en una lista)  (se puede enviar a diferentes personas si colocas los destinatarios
				en una lista)"""


				return "Se envio correctamente." 


			except:
				return "No se pudo enviar el mensaje."


		else:

			try:
				self.conexion.send(destino, asunto, mensaje)


				return "Se envio correctamente." 


			except:
				return "No se pudo enviar el mensaje."


		self.conexion.close()
		



