from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Dict, Optional
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da API OpenAI
cliente = OpenAI()
modelo: str = "gpt-4"  # Troque para "gpt-4" se tiver acesso

# Dicionário de personas baseado no sentimento
personas: Dict[str, str] = {
    "positivo": """
        Você é um Entusiasta Ecológico, um atendente virtual da Longitude Incorporadora. Você sempre responde de forma otimista e positiva, destacando os aspectos sustentáveis e inovadores da empresa.
        Além disso, você tem acesso a ferramentas que permitem pesquisar informações detalhadas nos documentos disponíveis da empresa.
    """,
    "neutro": """
        Você é um Informante Pragmático, um atendente virtual da Longitude Incorporadora. Você fornece informações claras e objetivas, sem emoções intensas, focando nos fatos e dados relevantes sobre a empresa.
        Além disso, você tem acesso a ferramentas que permitem pesquisar informações detalhadas nos documentos disponíveis da empresa.
    """,
    "negativo": """
        Você é um Solucionador Compassivo, um atendente virtual da Longitude Incorporadora. Você responde de maneira empática e compreensiva, focando em resolver problemas e atender às necessidades dos clientes de forma eficaz.
        Além disso, você tem acesso a ferramentas que permitem pesquisar informações detalhadas nos documentos disponíveis da empresa.
    """
}

# Prompt do sistema para análise de sentimento
PROMPT_SISTEMA = """
Faça uma análise da mensagem informada abaixo para identificar se o sentimento é: positivo, neutro ou negativo. 
Retorne apenas uma das três palavras: "positivo", "neutro" ou "negativo".
"""

def selecionar_persona(mensagem_usuario: str) -> str:
    """
    Analisa a mensagem do usuário e retorna a persona correspondente ao sentimento detectado.

    :param mensagem_usuario: A mensagem do usuário a ser analisada.
    :return: Uma string com o sentimento detectado ("positivo", "neutro" ou "negativo").
    """
    if not mensagem_usuario or not isinstance(mensagem_usuario, str):
        logger.warning("Mensagem do usuário inválida ou vazia.")
        return "neutro"  # Valor padrão

    try:
        resposta = cliente.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {"role": "user", "content": mensagem_usuario},
            ],
            temperature=0.7,  # Reduzido para respostas mais consistentes
        )

        sentimento = resposta.choices[0].message.content.lower()

        # Valida se o sentimento é válido
        if sentimento not in personas:
            logger.warning(f"Sentimento inesperado retornado: {sentimento}")
            return "neutro"  # Valor padrão

        return sentimento

    except Exception as e:
        logger.error(f"Erro ao chamar a API da OpenAI: {e}")
        return "neutro"  # Valor padrão em caso de erro