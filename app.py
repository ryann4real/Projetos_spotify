import streamlit as st

import os
os.system("cls")


musicas = {
    "alee":{
        "Pente Longo":"https://www.youtube.com/watch?v=pJ238BsWr-0",
        "Tudo de novo":"https://www.youtube.com/watch?v=1Qus1HEB_fA"
    },

    "Matue":{
        "333":"https://www.youtube.com/watch?v=aq-DH4iwviE",
        "Gorila roxo":"https://www.youtube.com/watch?v=BUL7zecHZjA"
    },

    "Leviano":{
        "mil a menos, mil a mais":"https://www.youtube.com/watch?v=hwoobdugnC8",
        "BUSIIINESSS":"https://www.youtube.com/watch?v=M_GAHSd-UQI&list=PLxA687tYuMWjIKofEzdHpkp7YwbQreGeo&index=6"
    },
    "Dfideliz":{
        "Essa noite eu bebi amor":"https://www.youtube.com/watch?v=bmsILfH-UOw",
        "Mulher":"https://www.youtube.com/watch?v=XnobfnCsieA"
    },
    "Frank ocean":{
        "Nights":"https://www.youtube.com/watch?v=r4l9bFqgMaQ",
        "Pink Matter":"https://www.youtube.com/watch?v=uaLV003llhY"
    },
    "Daniel caesar":{
        "Get You":"https://www.youtube.com/watch?v=uQFVqltOXRg",
        "Always":"https://www.youtube.com/watch?v=pKFd12id5oQ"
    }
}   
    

st.sidebar.image("logo.png")
artistas = st.sidebar.selectbox("Selecione o artissta", musicas.keys())
musicas_artista = musicas[artistas]
st.title(artistas)
for musica in musicas_artista.items():
    titulo,link = musica
    st.subheader(titulo)
    st.video(link)