meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso","LOL": "Una respuesta común a algo gracioso", "IDK": "significa no se", "XD": "significa mucha risa"}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict [word])
else:
    print("esa palabra aun no esta, o la escribiste mal")
