import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
#from  PIL import Image
#import numpy as np
#import cv2
#import pandas as pd
#from st_aggrid import AgGrid
#import plotly.express as px
import io 

#import streamlit_autorefresh as st_autorefresh
#count = st_autorefresh(interval=2000, limit=100, key="frizzbuzzcounter")

choose = option_menu("Frankie", ["Treinar modelo", "Ajustar parâmetros", "Executar"],
                     icons=['house', 'gear', 'play-circle-fill'],
                     menu_icon="robot", default_index=0,
                     orientation="horizontal",
                     styles={
    "container": {"padding": "5!important", "background-color": "#fafafa"},
    "icon": {"color": "orange", "font-size": "25px"}, 
    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #"nav-link-selected": {"background-color": "#02ab21"},
    "nav-link-selected": {"background-color": "#2e5cb8"},
}
)

if choose == "Treinar modelo":
    st.write("## Capture as imagens")
    st.number_input("Informe a quantidade de classes", 1, value=4)
    st.number_input("Informe a quantidade imagens de treinamento por classe", 1, value=10)
    if st.button("Iniciar câmera"):
        img_file_buffer = st.camera_input("")

        if img_file_buffer is not None:
            # To read image file buffer as bytes:
            bytes_data = img_file_buffer.getvalue()
            # Check the type of bytes_data:
            # Should output: <class 'bytes'>
            st.write(type(bytes_data))
elif choose == "Ajustar parâmetros":
    confianca = st.select_slider("Confiança", np.arange(0,1.0025,0.0025), value=0.2, format_func = lambda x: f"{x*100:.2f}%")
    tuplas = st.slider("Tuplas", 3, 8, 5)
    velocidade_d = st.number_input("Velocidade (direita)", value=75)
    velocidade_e = st.number_input("Velocidade (esquerda)", value=75)
elif choose == "Executar":
    st.write("## Executar")
    st.button("Começar! 🚀")
