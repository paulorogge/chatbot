```
CHATBOT
Este projeto demonstra como rodar modelos de IA localmente utilizando DeepSeek com o LM Studio.

📌 Requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados:
Python (versão 3.8 ou superior)
Pip atualizado (pip install --upgrade pip)
LM Studio instalado (Baixar LM Studio)

⚙️ Configuração do Ambiente
No Windows:
python -m venv chatbot
Ativando o Ambiente Virtual
chatbot\Scripts\activatet\Scripts\activate


📦 Instalação das Dependências
Execute o seguinte comando para instalar as bibliotecas necessárias:
pip install numpy openai python-dotenv tiktoken flask opencv-python

🧠 Configuração do LM Studio
O projeto utiliza DeepSeek, versão deepseek-r1-distill-qwen-7b, rodando localmente via LM Studio.

📌 Executando o Projeto
Para rodar a aplicação, utilize:

python app.py


📂 chatbot/
│── 📂 static/              # Arquivos estáticos (CSS, JS, imagens)
│── 📂 templates/           # Templates HTML para a aplicação Flask
│── 📂 services/            # Serviços auxiliares do projeto
│── 📂 dados/               # Base de dados e arquivos de contexto
│── ├── app.py             # Arquivo principal da aplicação
│── ├── config.py          # Configuração da aplicação
│── ├── helpers.py         # Funções auxiliares
│── ├── selecionar_persona.py  # Módulo para escolher personas
│── ├── selecionar_contexto.py # Módulo para escolher contexto
│── ├── assistente_local.py    # Lógica do chatbot local
│── ├── requirements.txt   # Lista de dependências
│── ├── .gitignore         # Arquivos ignorados pelo Git
│── ├── README.md          # Este arquivo 😃
