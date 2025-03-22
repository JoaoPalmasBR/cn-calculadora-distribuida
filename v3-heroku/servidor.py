import os
import socket
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configuração do logger
logging.basicConfig(level=logging.INFO)

# Função para calcular expressões matemáticas
def calcular(expressao):
    try:
        resultado = eval(expressao, {"__builtins__": None}, {})
        return str(resultado)
    except Exception as e:
        return f"Erro: {str(e)}"

# Rota de API para calcular expressões matemáticas
@app.route('/calcular', methods=['POST'])
def calcular_api():
    data = request.get_json()
    expressao = data.get('expressao')

    if expressao:
        resultado = calcular(expressao)
        return jsonify({"resultado": resultado})
    else:
        return jsonify({"erro": "Expressão não fornecida"}), 400

# Iniciar o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
