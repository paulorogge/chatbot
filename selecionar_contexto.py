import os

def selecionar_contexto(prompt: str) -> str:
    """
    Função para selecionar o contexto com base nos arquivos .txt.
    """
    TXT_FOLDER = "dados/contexto/"  # Substitua pelo caminho da pasta com os arquivos .txt
    conteudo = ""

    # Lê todos os arquivos .txt na pasta
    for arquivo in os.listdir(TXT_FOLDER):
        if arquivo.endswith(".txt"):
            with open(os.path.join(TXT_FOLDER, arquivo), "r", encoding="utf-8") as f:
                conteudo += f.read() + "\n"

    return conteudo