// main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import Registration from './components/Registration'; // Import the Registration component
import './index.css';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Registration /> {/* Render the Registration component */}
  </React.StrictMode>,
);
