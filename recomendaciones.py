from clasificacion_emociones import clasificar_emocion

def generar_recomendacion(clasificar_emocion):
    if clasificar_emocion == "tristeza":
        return ["Te recomiendo escuchar música alegre o ver una película divertida.",
                "Intenta practicar la gratitud escribiendo en un diario las cosas por las que estás agradecido.",
                "Habla con un amigo cercano o un ser querido sobre tus sentimientos para sentirte apoyado."]
    elif clasificar_emocion == "alegría":
        return ["Te recomiendo salir a caminar o hacer ejercicio.",
                "Organiza una reunión con amigos o familiares para compartir momentos de felicidad.",
                "Haz algo creativo que te apasione, como pintar, cocinar o escribir."]
    elif clasificar_emocion == "ira":
        return ["Te recomiendo tomar algunas respiraciones profundas y practicar técnicas de relajación.",
                "Haz ejercicio físico para liberar la energía acumulada.",
                "Escribe una carta expresando tus sentimientos de ira, pero no la envíes, solo desahógate."]
    elif clasificar_emocion == "miedo":
        return ["Te recomiendo hablar con un amigo o familiar sobre tus preocupaciones.",
                "Practica la meditación o el mindfulness para calmar la mente y reducir la ansiedad.",
                "Haz una lista de tus miedos y trabaja en desafiarlos gradualmente para superarlos."]
    elif clasificar_emocion == "amor":
        return ["Te recomiendo pasar tiempo de calidad con tus seres queridos y expresar tus sentimientos abiertamente.",
                "Haz algo especial para mostrar tu aprecio hacia quienes amas, como prepararles una comida o escribirles una carta de amor.",
                "Practica la empatía y la compasión al poner en práctica pequeños actos de bondad hacia los demás."]
    else:
        return ["No tengo una recomendación específica para esta emoción."]

#def generar_recomendacion_personalizada(emocion, edad, sexo, intereses):
# Implementar lógica para generar recomendaciones personalizadas
# ...

# return "Recomendación personalizada: ..."

