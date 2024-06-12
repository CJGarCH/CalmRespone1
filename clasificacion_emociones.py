from joblib import load
import keras
from keras.models import load_model
from sklearn.feature_extraction.text import HashingVectorizer
import joblib
from keras_preprocessing.text import Tokenizer
import numpy as np
from sklearn.pipeline import Pipeline
import prueba
from prueba import preprocess_text

tokenizer = Tokenizer()

def clasificar_emocion(texto):
    """
    Clasifica la emoción del texto dado.

    Args:
        texto: El texto a clasificar.

    Returns:
        La emoción predicha.
    """

    try:
        texto_preprocesado = prueba.preprocess_text([texto])
        # Cargar el vectorizador HashingVectorizer ajustado
        vectorizer = load("vectorizer_entrenado.pkl")

        # Transformar el texto usando el vectorizador ajustado
        X = vectorizer.transform(texto_preprocesado)

        # Cargar el modelo entrenado
        model = load("modelo_entrenado.pkl")
        print("Modelo cargado correctamente.")

        # Predecir la emoción
        probabilidades = model.predict(X)
        print("Probabilidades:", probabilidades)

         # Predecir la emoción como el índice con la mayor probabilidad
        #emocion_predicha = np.argmax(probabilidades)

        # Mapear el valor numérico de la emoción a su etiqueta correspondiente
        #emociones_dict = {0: 'tristeza', 1: 'alegría', 2: 'amor', 3: 'ira', 4: 'miedo'}
        emocion_predicha = probabilidades

        # Devolver la emoción predicha como una cadena
        return emocion_predicha

    except Exception as e:
        # Manejar el error
        print(f"Error al predecir la emoción: {e}")

        # Si hay un error, devolver "No se puede predecir"
        return "No se puede predecir"


def prueba_clasificacion():
    textos_prueba = [
        "Estoy muy feliz hoy",
        "Me siento muy triste por lo sucedido",
        "Estoy lleno de amor por mi familia",
        "Me enfurece la injusticia que veo",
        "Siento mucho miedo cuando estoy solo por la noche"
    ]

    for texto in textos_prueba:
        emocion_predicha = clasificar_emocion(texto)
        print(f"Texto: '{texto}', Emoción predicha: {emocion_predicha}")

# Ejecutar la función de prueba
prueba_clasificacion()