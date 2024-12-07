import random
datos= ["computadora","carro","velocidad","fuerza","felicidad","tristeza","vida"]
meme_dict = {"velocidad": "es el cambio de posicion de un objeto con respecto al tiempo",
            "carro": "Vehiculo o armazon con ruedas que se emplea para transportar objetos",
            "computadora": "maquina electronica que puede procesar y almacenar informacion",
            "fuerza": "accion que permite que un objeto se mueva o cambie de forma",
            "felicidad": " es una emocion o estado de animo que experimenta un ser consciente cuando llega a un momento de conformacion, bienestar o se han conseguido ciertos objetivos deseables para el individuo consciente",
            "tristeza": "Sensacion de decaimiento o infelicidad en respuesta a una afliccion, desanimo o desilusion",
            "trabajo": "Esfuerzo humano aplicado a la produccion de riqueza, en contraposicion a capital.",
            "vida": "Fuerza o actividad esencial mediante la que obra el ser que la posee"}

word = input("Escribe una palabra que no entiendas: ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("la palabra no esta en el dixionario")

pDate = random.choice(datos)

print(pDate)