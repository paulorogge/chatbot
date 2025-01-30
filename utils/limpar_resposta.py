import re

def limpar_resposta(resposta: str) -> str:
    """
    Remove quebras de linha e qualquer conteúdo dentro das tags <think></think>.
    """
    # Remove quebras de linha
    resposta = resposta.replace("\n", " ")

    # Remove conteúdo dentro de <think>...</think>
    resposta = re.sub(r"<think>.*?</think>", "", resposta, flags=re.DOTALL)

    # Remover espaços extras caso fiquem na resposta final
    return resposta.strip()