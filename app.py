from flask import Flask, request, jsonify
from flask_cors import CORS , cross_origin # Importa el complemento CORS
import pandas as pd
import clasificacion_emociones as ce
import recomendaciones as re

app = Flask(__name__)
cors=CORS(app, resources={r'/*'})  # Habilita CORS para todas las rutas

def guardar_respuesta_csv(texto, emocion_predicha):
    try:
        df = pd.read_csv("respuestas_emergencia.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Texto", "Emocion"])

    nueva_fila = pd.DataFrame({"Texto": [texto], "Emocion": [emocion_predicha]})
    df = pd.concat([df, nueva_fila], ignore_index=True)
    
    try:
        df.to_csv("respuestas_emergencia.csv", index=False)
    except Exception as e:
        print(f"Error al guardar la respuesta: {e}")
        
@cross_origin
@app.route('/emergency', methods=['POST'])
def emergency():
    data = request.json
    print(f"Data received: {data}")  # Debug print
    texto = data.get('texto')
    if not texto:
        print("Texto no proporcionado")  # Debug print
        return jsonify({'error': 'Texto no proporcionado'}), 400

    try:
        emocion_predicha = ce.clasificar_emocion(texto)
        recomendacion = re.generar_recomendacion(emocion_predicha)

        print(f"Emocion predicha: {emocion_predicha}, Tipo: {type(emocion_predicha)}")  # Debug print
        print(f"Recomendacion: {recomendacion}, Tipo: {type(recomendacion)}")  # Debug print

        # Asegurarse de que son listas
        if not isinstance(emocion_predicha, list):
            emocion_predicha = list(emocion_predicha)
        if not isinstance(recomendacion, list):
            recomendacion = list(recomendacion)

        print(f"Emocion predicha (post-conversion): {emocion_predicha}, Tipo: {type(emocion_predicha)}")  # Debug print
        print(f"Recomendacion (post-conversion): {recomendacion}, Tipo: {type(recomendacion)}")  # Debug print

        guardar_respuesta_csv(texto, emocion_predicha)

        response = jsonify({'emotion': emocion_predicha, 'recommendation': recomendacion})
        print(f"Response: {response.get_json()}")  # Debug print
        return response

    except Exception as e:
        print(f"Error en el procesamiento: {e}")  # Debug print
        return jsonify({'error': 'Error en el procesamiento'}), 500


@app.route('/survey', methods=['POST'])
def survey():
    data = request.json
    respuestas = data.get('respuestas')
    if not respuestas or len(respuestas) != 5:
        return jsonify({'error': 'Respuestas no proporcionadas o incompletas'}), 400

    if "sí" in respuestas[-1]:
        recomendacion = "Necesita una cita prioritaria de salud mental. Por favor, programe una cita lo antes posible."
    elif "sí" in respuestas[:2]:
        recomendacion = "Necesita una cita de salud mental en los próximos dos o tres días."
    else:
        recomendacion = "Puede esperar un poco más, pero no dude en buscar ayuda si sus síntomas empeoran."

    return jsonify({'recommendation': recomendacion})

if __name__ == '__main__':
    app.run(debug=True)
