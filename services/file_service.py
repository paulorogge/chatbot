import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def carregar_arquivos(caminho: str) -> str:
    """
    Carrega o conteúdo de um arquivo .txt.
    Retorna uma string vazia se o arquivo não existir.
    """
    conteudo = ""
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
        except Exception as e:
            logger.error(f"Erro ao ler o arquivo {caminho}: {e}")
    else:
        logger.warning(f"Arquivo não encontrado: {caminho}")
    return conteudo