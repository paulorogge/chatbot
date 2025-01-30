import os

# Caminho para a pasta de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório do script atual
DADOS_DIR = os.path.join(BASE_DIR, "dados")  # Pasta "dados"
CONTEXTO_DIR = os.path.join(DADOS_DIR, "contexto")  # Pasta "contexto"

# Cria as pastas se não existirem
os.makedirs(DADOS_DIR, exist_ok=True)
os.makedirs(CONTEXTO_DIR, exist_ok=True)

# Lista de arquivos para carregar
ARQUIVOS = [
    os.path.join(CONTEXTO_DIR, "longitude_incorporadora.txt"),
    os.path.join(CONTEXTO_DIR, "dados_longitude_incorporadora.txt"),
    os.path.join(CONTEXTO_DIR, "políticas_longitude_incorporadora.txt"),
    os.path.join(CONTEXTO_DIR, "produtos_longitude_incorporadora.txt")
]

# Configurações do LM Studio
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"  # URL do servidor local do LM Studio