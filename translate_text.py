from googletrans import Translator		#para traducir





def trans_text(text_trans, lang = "es"):
	
	
	translator = Translator()	#iniciamos el traductor

	result = translator.translate(text = text_trans, dest = lang)	#traducira el texto al idioma indicado (dest = "idioma")

	return result.text




def trans_all_text(all_text, lang = "es"):
	

	strings = {}


	translator = Translator()	#iniciamos el traductor


	#traducimos uno a uno los texto de la lista
	for trans in all_text:
		

		result = translator.translate(text = trans, dest = lang)


		strings[trans] = result.text


	#devolvemos un diccionario con la frase original y la traduccion pedida
	return strings




print(trans_text("hello world"))



