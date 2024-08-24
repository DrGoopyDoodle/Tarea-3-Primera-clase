meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "TQM": "Te quiero mucho",
            "XD": "Emoticono para mostrar risa o diversión"
            }
print("Hola, esto es un diccionario para entender las palabras que no entiendes, haslo 3 veces")
for i in range(3):
    word = input("Escribe una palabra (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Mmmm.., no lo hemos encontrado,INTENTA DE NUEVO o REINICIA el programa")
print("Listo! si quieres ver mas palabras reinicia el programa")
