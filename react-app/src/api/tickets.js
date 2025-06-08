import axios from 'axios';

const API_URL = window.electron ? await window.electron.getApiUrl() : 'http://localhost:5000';

export const sendTicket = async (ticketData) => {
  const response = await axios.post(`${API_URL}/tickets`, ticketData, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    }
  });
  return response.data;
};

export const getTickets = async (department) => {
  const response = await axios.get(`${API_URL}/tickets`, {
    params: { department },
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    }
  });
  return response.data;
};