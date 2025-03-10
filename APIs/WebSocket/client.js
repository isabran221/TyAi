const WebSocket = require('ws');
const ws = new WebSocket('ws://localhost:8080');

ws.on('open', () => {
    ws.send('Hola servidor');
});

ws.on('message', message => {
    console.log(`Respuesta: ${message}`);
});
