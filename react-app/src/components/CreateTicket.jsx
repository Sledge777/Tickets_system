import React, { useState } from 'react';
import { Box, TextField, Button, Typography, CircularProgress } from '@mui/material';
import { sendTicket } from '../api/tickets';

export function CreateTicket() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!title.trim() || !description.trim()) {
      setError('Заполните все поля');
      return;
    }

    setIsLoading(true);
    try {
      await sendTicket({ title, description });
      setTitle('');
      setDescription('');
      setError('');
      alert('Тикет успешно создан!');
    } catch (err) {
      setError('Ошибка при отправке: ' + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box sx={{ p: 3, maxWidth: 600, margin: '0 auto' }}>
      <Typography variant="h4" gutterBottom>Новый тикет</Typography>
      
      <TextField
        label="Заголовок"
        fullWidth
        margin="normal"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      
      <TextField
        label="Описание проблемы"
        fullWidth
        multiline
        rows={4}
        margin="normal"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      
      {error && <Typography color="error">{error}</Typography>}
      
      <Button
        variant="contained"
        onClick={handleSubmit}
        disabled={isLoading}
        sx={{ mt: 2 }}
      >
        {isLoading ? <CircularProgress size={24} /> : 'Отправить'}
      </Button>
    </Box>
  );
}