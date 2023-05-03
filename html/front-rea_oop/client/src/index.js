import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter} from 'react-router-dom';
import { AuthProvider } from "./context/auth"
import { RoomProvider } from './context/room';
import { DataProvider } from './context/data';
import { LastProvider } from './context/lastprice';
import { AddonsProvider } from './context/addonsshow';
import { SystemProvider } from './context/system';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <SystemProvider>
  <AddonsProvider>
  <LastProvider>
  <DataProvider>
  <RoomProvider>
  <AuthProvider>
  <BrowserRouter>
  <React.StrictMode>
    <App />
  </React.StrictMode>
  </BrowserRouter>
  </AuthProvider>
  </RoomProvider>
  </DataProvider>
  </LastProvider>
  </AddonsProvider>
  </SystemProvider>

);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
