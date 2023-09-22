from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import ssl
import smtplib
import re





class Enviar_Correo():

	direccion = "@gmail.com"
	mi_direccion = "---------@gmail.com"	#correo gmail
	mi_contrasenna = "---------------"		#contraseña de aplicaciones para gmail

	



	def envio(self, archivo, usuario, a_enviar):

		if re.findall("[_]", usuario) or re.findall("[@]", usuario):	#comprueba si cumple las condiciones
			return "la direccion no puede llevar 2 o mas (_) o (@)"


		else:
			correo = usuario + self.direccion


			mail = MIMEMultipart()	#creamos el objeto mensaje


			#INGRESAMOS LOS DATOS 
			mail["From"] = self.mi_direccion
			mail["To"] = correo
			mail["Subject"] = "envio de mail"

		
			if archivo == False:	#True seria enviar una imagen y False solo texto
				mail.attach(MIMEText(a_enviar, "plain"))	#agregamos el mensaje de texto que se enviara


			else:
				#leemos una imagen para luego ser enviada
				file = open(a_enviar, "rb")
				imagen = MIMEImage(file.read())
				mail.attach(imagen)	 #agregamos la imagen a enviar


			conexion = ssl.create_default_context()	 #para que halla una conexion segura entre 2 puertos(Datas)


			try:
				with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = conexion) as smtp:	#nos conectamos al servidor

					smtp.login(self.mi_direccion, self.mi_contrasenna)	#nos logeamos
					smtp.sendmail(self.mi_direccion, correo, mail.as_string())	 #enviamos el correo deseado
					smtp.quit()


					return "mensaje enviado con Exito"


			except: 
				return "no se pudo enviar el mensaje"


				
		

e = Enviar_Correo()

print(e.envio(False, "jesusCristo001", "hola a todos"))	  # 1. si es imagen o no || 2. usuario de correo gmail(sin el @gmail.com) || 3. el mensaje de texto o imagen a enviar 
