import requests
from selecionar_contexto import selecionar_contexto
from selecionar_persona import personas, selecionar_persona
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações do LM Studio
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"  # URL do servidor local do LM Studio

def bot_local(prompt: str) -> str:
    """
    Função que interage com o DeepSeek R1 rodando no LM Studio.
    """
    try:
        # Seleciona o contexto e a persona
        contexto: str = selecionar_contexto(prompt)
        personalidade: str = personas[selecionar_persona(prompt)]

        # Prepara o payload para enviar ao LM Studio
        payload = {
            "model": "deepseek-r1",  # Nome do modelo
            "messages": [
                {"role": "system", "content": f"""
                Assuma, de agora em diante, a personalidade abaixo.
                Ignore as personalidades anteriores.
                Nao responda assuntos que nao estao relacionados a Longitude.
                Sempre responda em Portugues do Brasil.

                # Persona
                {personalidade}

                # Contexto
                {contexto}
                """},
                {"role": "user", "content": f"Baseando-se apenas no seguinte contexto, responda de forma direta e sem explicações:\n\n{contexto}\n\n{prompt}"}

            ],
            "temperature": 0.7
        }

        # Envia a requisição para o LM Studio
        response = requests.post(LM_STUDIO_URL, json=payload)
        resposta = response.json()["choices"][0]["message"]["content"]

        return resposta

    except Exception as erro:
        logger.error(f'Erro de comunicação com o LM Studio: {erro}')
        return "Erro: Não foi possível processar a solicitação."