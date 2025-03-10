const WebSocket = require('ws');
const server = new WebSocket.Server({ port: 8080 });

server.on('connection', ws => {
    ws.on('message', message => {
        console.log(`Mensaje recibido: ${message}`);
        ws.send(`Eco: ${message}`);
    });
});
