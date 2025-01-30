from flask import Flask, jsonify, request, render_template, Response
from services.assistant_service import carregar_contexto
from services.deepseek_service import perguntar_ao_deepseek
import logging
import json

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint que recebe JSON {"msg": "..."} e retorna a resposta do bot.
    """
    data = request.get_json()

    if not data or "msg" not in data:
        logger.warning("Nenhum prompt fornecido na requisição.")
        return jsonify({"erro": "Nenhum prompt fornecido"}), 400

    prompt = data["msg"].strip()

    if not prompt:
        logger.warning("Prompt vazio recebido.")
        return jsonify({"erro": "Prompt vazio"}), 400

    try:
        logger.info(f"Recebendo prompt: {prompt}")

        # Carrega o contexto dos arquivos .txt
        contexto = carregar_contexto()

        # Envia a pergunta e o contexto para o DeepSeek
        resposta = perguntar_ao_deepseek(prompt, contexto)

        logger.info(f"Resposta gerada: {resposta}")

        return Response(resposta, content_type="text/plain; charset=utf-8")

    except ValueError as ve:
        logger.error(f"Erro de valor: {ve}")
        return jsonify({"erro": "Erro ao processar a entrada"}), 400
    except Exception as e:
        logger.exception("Erro interno no servidor")
        return jsonify({"erro": "Erro interno no servidor"}), 500

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
