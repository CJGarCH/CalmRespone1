// src/components/SurveyButton.tsx
import React, { useState } from 'react';
import axios from 'axios';

const questions = [
  "¿Has experimentado cambios en tu apetito últimamente?",
  "¿Has tenido problemas para conciliar el sueño o has dormido demasiado?",
  "¿Te has sentido constantemente preocupado o nervioso?",
  "¿Has perdido interés en actividades que solías disfrutar?",
  "¿Has tenido pensamientos recurrentes sobre la muerte o el suicidio?"
];

const SurveyButton: React.FC = () => {
  const [respuestas, setResponses] = useState<string[]>(Array(questions.length).fill(''));
  const [recommendation, setRecommendation] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/survey', { respuestas });
      setRecommendation(response.data.recommendation);
    } catch (error) {
      console.error('Error durante el envío de la encuesta:', error);
    }
  };

  const handleResponseChange = (index: number, value: string) => {
    const newResponses = [...respuestas];
    newResponses[index] = value;
    setResponses(newResponses);
  };

  return (
    <div>
      <h2>Encuesta de Salud Mental</h2>
      <form onSubmit={handleSubmit}>
        {questions.map((question, index) => (
          <div key={index}>
            <label>
              {question}
              <select
                value={respuestas[index]}
                onChange={(e) => handleResponseChange(index, e.target.value)}
              >
                <option value="">Si/No</option>
                <option value="sí">Sí</option>
                <option value="no">No</option>
              </select>
            </label>
          </div>
        ))}
        <button type="submit">Enviar</button>
      </form>
      {recommendation && (
        <div>
          <p>Recomendación: {recommendation}</p>
        </div>
      )}
    </div>
  );
};

export default SurveyButton;
