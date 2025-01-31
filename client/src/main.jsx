// import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import React, { StrictMode } from "react";
import {Provider} from "react-redux";
import './index.css'
import App from './App.jsx'
import store from "./store"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </StrictMode>
);

