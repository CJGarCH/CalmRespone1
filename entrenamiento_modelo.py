import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def entrenar_modelo_emergencia(respuestas_emergencia):

    # Extraer textos y emociones de las respuestas
    textos = [respuesta[0] for respuesta in respuestas_emergencia]
    emociones = [respuesta[1] for respuesta in respuestas_emergencia]

    # Crear y ajustar el vectorizador TF-IDF
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(textos)

    # Crear un modelo de Regresión Logística
    clf = LogisticRegression()

    # Entrenar el modelo
    clf.fit(X_train, emociones)

    # Evaluar el rendimiento del modelo (opcional)
    # X_test, y_test = train_test_split(X_train, emociones, test_size=0.25)
    # accuracy = accuracy_score(clf.predict(X_test), y_test)
    # print(f"Precisión del modelo: {accuracy:.2f}")

    # Guardar el vectorizador y el modelo ajustados
    joblib.dump(vectorizer, "vectorizer.pkl")
    joblib.dump(clf, "modelo_emergencia.pkl")


