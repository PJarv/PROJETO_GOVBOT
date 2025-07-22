const express = require('express');
const app = express();
const http = require('http');
const server = http.Server(app);
const io = require('socket.io')(server);
const port = process.env.PORT || 3000;

const URL_GOVBOT = "http://localhost:6000/response/";
const CONFIANCA_MINIMA = 0.65;

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

function getResponse(message) {
  let data = "";

  http.get(URL_GOVBOT + encodeURIComponent(message), (res) => {
    res.on("data", (chunk) => {
      data += chunk;
    });

    res.on("end", () => {
      try {
        const parsed = JSON.parse(data);
        if (parsed.confidence >= CONFIANCA_MINIMA) {
          io.emit('chat message', parsed.response);
        } else {
          io.emit('chat message', "Não entendi bem essa pergunta. Para mais informações, acesse o Portal Gov.br em https://www.gov.br");
        }
        console.log(parsed);
      } catch (error) {
        console.error("Erro ao processar a resposta:", error);
      }
    });
  }).on("error", (err) => {
    console.error("Erro na requisição HTTP:", err);
  });
}

io.on('connection', (socket) => {
  socket.on('chat message', (msg) => {
    io.emit('chat message', msg);
    getResponse(msg);
  });
});

server.listen(port, () => {
  console.log('listening on *:' + port);
});
