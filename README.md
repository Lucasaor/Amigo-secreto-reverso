# Amigo Secreto Reverso

## Descrição
O Amigo Secreto Reverso é uma variação divertida do tradicional jogo de amigo secreto. Neste jogo, ao invés de tentar fazer os outros adivinharem quem é o seu "amigo secreto", você vai fazer perguntas geradas pela IA para descobrir quem é o seu "amigo secreto". As respostas da IA podem ser inesperadas, adicionando um elemento de surpresa e diversão ao jogo. A identidade do doador é revelada apenas no final, garantindo momentos de suspense e risadas.

## Funcionalidades
- Geração de Perguntas por IA: Utiliza uma IA para gerar perguntas divertidas e inesperadas que ajudam os jogadores a descobrir quem é o seu "amigo secreto".
- Histórico de Perguntas: Mantém um histórico das perguntas já feitas para evitar repetições.
- Interface Interativa: Utiliza o Streamlit para criar uma interface de usuário interativa e fácil de usar.

## Requisitos
- Python 3.x
- `streamlit`, `langchain`, `openai`
- É necessário utilizar uma API da OpenAI. Pode ser adaptado para usar o Ollama também, mas ainda sem suporte.

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/lucasaor/amigo-secreto-reverso.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd amigo-secreto-reverso
    ```
3. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    ```
4. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Use o arquivo `example.env` como exemplo para criar um arquivo .env contendo uma chave válida para Open AI. o arquivo deve a seguinte estrutura:
    ```
    OPENAI_API_KEY=SUA_CHAVE_DA_OPENAI_AQUI
    ```


## Uso
1. Inicie o aplicativo Streamlit:
    ```bash
    streamlit run app.py
    ```
2. Acesse o aplicativo no navegador:
    ```
    http://localhost:8501
    ```

## Contribuição
1. Faça um fork do projeto
2. Crie uma branch para sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Commit suas mudanças:
    ```bash
    git commit -m 'Adiciona minha feature'
    ```
4. Faça um push para a branch:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.