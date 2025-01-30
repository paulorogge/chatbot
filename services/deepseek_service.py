import requests
from config import LM_STUDIO_URL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import re

def limpar_resposta(resposta: str) -> str:
    """
    Remove quebras de linha desnecessárias e melhora a formatação da resposta.
    - Remove `<think>...</think>`.
    - Garante que cada item numerado fique em uma linha separada.
    """
    # Remove tags <think>...</think>
    resposta = re.sub(r"<think>.*?</think>", "", resposta, flags=re.DOTALL)

    # Adiciona quebra de linha antes dos números da lista (1., 2., 3., etc.)
    resposta = re.sub(r"(\d+\.)", r"\n\1", resposta)

    # Remove espaços extras e retorna a resposta formatada
    return resposta.strip()

def perguntar_ao_deepseek(prompt: str, contexto: str) -> str:
    try:
        payload = {
            "model": "deepseek-r1-distill-qwen-7b",
            "messages": [
                {"role": "system", "content": "Apenas forneça a resposta final, sem qualquer pensamento ou raciocínio sobre a pergunta. Não explique sua resposta. Responda de forma curta e objetiva."},
                {"role": "user", "content": f"Baseando-se apenas no seguinte contexto, responda de forma direta e sem explicações:\n\n{contexto}\n\n{prompt}"}
            ],
            "temperature": 0.1
        }

        response = requests.post(LM_STUDIO_URL, json=payload)
        response_data = response.json()

        if "choices" in response_data and len(response_data["choices"]) > 0:
            resposta = response_data["choices"][0]["message"]["content"]

            # Limpar a resposta antes de retorná-la
            resposta_limpa = limpar_resposta(resposta)
            return resposta_limpa

        logger.error("Resposta inesperada do LM Studio: %s", response_data)
        return "Erro: Resposta inesperada do modelo."

    except requests.RequestException as e:
        logger.error(f"Erro de comunicação com o LM Studio: {e}")
        return "Erro: Não foi possível se comunicar com o servidor."

    except Exception as e:
        logger.exception("Erro ao processar a resposta")
        return "Erro: Não foi possível processar a resposta."
