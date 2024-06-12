import React, { useState } from 'react';
import axios from 'axios';

interface EmergencyResponse {
  emotion: string[];
  recommendation: string[];
}
const EmergencyButton: React.FC = () => {
    const [text, setText] = useState('');
    const [recommendation, setRecommendation] = useState<string[]>([]);
    const [emotion, setEmotion] = useState<string[]>([]);
    
    console.log("Testt",text)
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post<EmergencyResponse>('http://127.0.0.1:5000/emergency', { texto: text });
      setEmotion(response.data.emotion);
      setRecommendation(response.data.recommendation);
    } catch (error) {
      console.error('Error durante el botón de emergencia:', error);
    }
  };

  return (
    <div>
      <h2>Botón de Emergencia</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Cuéntame cómo te sientes:
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </label>
        <button type="submit">Enviar</button>
      </form>
      {emotion.length > 0 && (
        <div>
          <p>Emoción Predicha: {emotion.join(', ')}</p>
          <p>Recomendación:</p>
          <ul>
            {recommendation.map((rec, index) => (
              <li key={index}>{rec}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default EmergencyButton;
