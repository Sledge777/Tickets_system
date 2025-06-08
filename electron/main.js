const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const isDev = !app.isPackaged;

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    },
    title: 'Ticket System',
    icon: path.join(__dirname, 'assets/icon.png')
  });

  // Загружаем React-приложение
  const startUrl = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../react-app/build/index.html')}`;
  
  mainWindow.loadURL(startUrl);

  // Открываем DevTools в development-режиме
  if (isDev) {
    mainWindow.webContents.openDevTools();
  }
}

app.whenReady().then(createWindow);

// IPC-канал для связи с React
ipcMain.handle('get-api-url', () => {
  return isDev ? 'http://localhost:5000' : 'https://your-production-api.com';
});