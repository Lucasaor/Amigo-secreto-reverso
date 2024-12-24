import streamlit as st
from llm import GeradorPerguntas
import time
import random
import json

def gerador_de_stream():
    if 'gerador' not in st.session_state:
        st.session_state.gerador = GeradorPerguntas()
    gerador = st.session_state.gerador
    pergunta = gerador.gerar_pergunta()

    for word in pergunta.split():
        yield word + " "
        time.sleep(0.05)

def main():
    st.title("Amigo Secreto Reverso 🎁")
    with st.expander("Regras do Jogo"):
        regras = """
        As regras do jogo são parecidas com o clássico "Amigo Secreto" brasileiro, mas com um plotwist. Em vez de tentar fazer os outros adivinharem quem é o seu "amigo secreto", 
        você vai fazer perguntas que a IA marota gerar para descobrir quem é o seu "amigo secreto". Já aviso que o programador que fez isso aqui estava totalmente marofado e fez em uma noite,
        então as respostas da IA podem ser meio nonsense. Boa sorte! (E sim, eu sei que o nome do jogo é meio bosta, mas é o que tem pra hoje)
        """
        st.write(regras)
    st.markdown("---")
    
    with open("prompts/perguntas_app.json", "r") as f:
        perguntas:list = json.load(f)
    
    st.write("👇🏽 Clica aqui para gerar a próxima pergunta.")
    if st.button("Gerar pergunta!"):
        with st.chat_message("AI"):
            st.write_stream(gerador_de_stream())
        st.session_state.pergunta_gerada = True

        st.markdown("---")
        st.write(random.choice(perguntas))

    
    st.write("Quando vc descobrir quem foi clica aqui embaixo")
    if st.button("Descobri! ✅"):
        if not st.session_state.pergunta_gerada:
            st.write("Descobriu bosta nenhuma não carai! Primeiro gera a pergunta ai")
        else:
            st.write("Aeee! até que enfim! 🎉")
            st.write("agora chama o proximo oreia seca ai")
            st.balloons()
            if st.button("Recomeçar"):
                st.session_state.gerador = GeradorPerguntas()
                st.session_state.descobriu = False
                st.session_state.pergunta_gerada = False
        

    

if __name__ == "__main__":
    main()

    

