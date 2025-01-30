def carrega(caminho: str) -> str:
    """
    Carrega o conteúdo de um arquivo.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()