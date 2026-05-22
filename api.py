import sys
import os
# Adiciona o diretório "agent-math" ao PYTHONPATH do script
sys.path.append(os.path.join(os.path.dirname(__file__), "agent-math"))

# Carrega as variáveis de ambiente do .env
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "agent-math", "agent_math", ".env"))

import math
import agent_math 

from flask import Flask, request, jsonify #type: ignore
from flask_cors import CORS #type: ignore

# importe seu agente aqui — ajuste conforme o nome do seu arquivo

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    # chame seu agente do mesmo jeito que você já faz hoje
    response = agent_math.run(user_message)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=8000, debug=True)