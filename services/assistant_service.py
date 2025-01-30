from services.file_service import carregar_arquivos
from config import ARQUIVOS

def carregar_contexto() -> str:
    """
    Carrega o contexto a partir dos arquivos .txt.
    """
    contexto = ""
    for arquivo in ARQUIVOS:
        contexto += carregar_arquivos(arquivo)
    return contexto