GovBot

Chatbot feito em Python com Flask e ChatterBot. Responde perguntas sobre serviços públicos como CPF, RG, alistamento, seguro-desemprego e Gov.br.

Instalação:

1. Clone o repositório:
    git clone https://github.com/PJarv/PROJETO_GOVBOT/tree/main
    cd govbot

2. Crie e ative o ambiente virtual:
    python -m venv venv
    venv\Scripts\activate  (Windows)
    source venv/bin/activate (Linux/macOS)

3. Instale as dependências:
    pip install -r requirements.txt

4. (Opcional) Se usar Node.js:
    npm install

Uso:

- Rodar API:
    cd api
    python service.py

- Treinar o bot:
    cd training
    python training.py

- Rodar testes:
    cd tests
    python tests.py
