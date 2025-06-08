import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import { TicketsList } from './components/TicketsList';
import { CreateTicket } from './components/CreateTicket'; 
import { Login } from './components/Login';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#1976d2' },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/tickets" element={<TicketsList />} />
          <Route path="/create" element={<CreateTicket />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;