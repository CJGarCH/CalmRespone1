from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from sklearn.preprocessing import FunctionTransformer

# Función para preprocesar el texto
def preprocess_text(text_list):
    processed_text = []
    for text in text_list:
        # Convertir a minúsculas
        text = text.lower()
        # Eliminar signos de puntuación
        text = ''.join(char for char in text if char.isalnum() or char.isspace())
        # Eliminar palabras vacías (stop words) y números
        stop_words = set(["a", "an", "the", "in", "on", "at", "for", "of", "by", "to", "and", "with", "without"])
        text = ' '.join(word for word in text.split() if word not in stop_words and not word.isdigit())
        processed_text.append(text)
    return processed_text

# Leer los datos
#data = []
#labels = []
#with open("training.csv", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            data.append(parts[0])  # Agregar la frase
            labels.append(int(parts[1]))  # Agregar la etiqueta
        else:
            print(f"Advertencia: La línea '{line.strip()}' no tiene suficientes elementos.")

# Mapear los números a las emociones correspondientes
emociones = {
    0: 'tristeza',
    1: 'alegría',
    2: 'amor',
    3: 'ira',
    4: 'miedo'
}
#labels = [emociones[label] for label in labels]

# Dividir los datos en conjuntos de entrenamiento y prueba
#X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Convertir cada lista de frases en X_train a cadenas de texto
#X_train_str = [str(row) for row in X_train]

# Crear un pipeline que incluya el preprocesamiento y la vectorización
#pipeline = Pipeline([
#    ('preprocessing', FunctionTransformer(preprocess_text)),
#    ('vectorizer', HashingVectorizer(n_features=1000, ngram_range=(1, 2), stop_words='english')),
#    ('classifier', LogisticRegression())  # Por ejemplo, un clasificador de regresión logística
#])

# Entrenar el pipeline con los datos de entrenamiento
#pipeline.fit(X_train_str, y_train)

# Evaluar el modelo entrenado
#y_pred = pipeline.predict(X_test)
#print(classification_report(y_test, y_pred))

# Guardar el modelo entrenado en un archivo .pkl
#joblib.dump(pipeline, 'vectorizer_entrenado.pkl')
