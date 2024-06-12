// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import EmergencyButton from './components/EmergencyButton';
import SurveyButton from './components/SurveyButton';
import './App.css'; // Importa el archivo CSS

const App: React.FC = () => {
  return (
    <Router>
      <div className="container">
      <Link to="/" className="logo-link">
          <img src="/logo.drawio-removebg-preview.png" alt="CalmResponse Logo" className="logo" />
        </Link>
        <nav className="navigation">
          <ul className="button-list">
            <li className="button-item">
              <Link to="/emergency" className="link-button">
                <button className="button">Botón de Emergencia</button>
              </Link>
            </li>
            <li className="button-item">
              <Link to="/survey" className="link-button">
                <button className="button">Encuesta de Salud Mental</button>
              </Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/emergency" element={<EmergencyButton />} />
          <Route path="/survey" element={<SurveyButton />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
