from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

class GeradorPerguntas:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(api_key=api_key)
        self.historico_perguntas = []

    def gerar_pergunta(self) -> str:
        with open("prompts/template.txt", "r") as f:
            contexto = f.read()
        
        # Adiciona o histórico de perguntas ao contexto
        contexto_completo = contexto + "\nHistórico de perguntas:\n" + "\n".join(self.historico_perguntas)
        
        mensagens = [
            SystemMessage(
            content=contexto_completo),
            HumanMessage(
            content="Gere a próxima pergunta"
            )
        ]
        resposta = self.llm.invoke(mensagens)
        
        # Armazena a pergunta gerada no histórico
        self.historico_perguntas.append(resposta.content)
        
        return resposta.content


