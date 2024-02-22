import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

##############
st.sidebar.image("stabledifussion777.png",
                 caption="Bienvenidx")



##############Pagina 1##############

def Inicio():
    st.markdown("# El_principito")
    st.sidebar.markdown("# El_principito")
    image = Image.open("elprincipito.jpeg")
    st.image(image, caption='El principito')

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('El principito ilustrado por ia')
        st.write('''Capacítate en skills que potencian tu CV.
        Implementa herramientas computacionales, simulaciones, 
        inteligencia artificial, prototipado con impresión 3D, y mucho más.''')
    with total2:
        st.info('En stock')
        st.write (pd.DataFrame({'Tipo': ['Físico, Tapa dura',
                                          'Físico, Tapa blanda', 
                                          'Digital'], 
                                'Inicio': ["S/ 60.00", "S/ 40.00", 
                                           "S/ 20.00"]}))
    image = Image.open("DALL·E 2022-12-26 21.10.51 - Humberto Maturana head for 3D printing.png")
    st.image(image, caption='Ilustración de personales literarios')
    
##############Pagina 2##############
def page2():
    st.markdown("# Mis creaciones")
    st.sidebar.markdown("# Mis creaciones")
    image = Image.open("alberteinstein.jpeg")
    st.image(image, caption='Taller')
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Mis ilustraciones')
        st.write('''Aprende a crear libros animados desde cero''')
        st.write (pd.DataFrame({'Temas': ['Python y redes neuronales artificiales',
                                  'Procesamiento de Lenguaje Natural', 
                                  'Llama 2 y ChatGPT'], 
                        'Horas': ["2 asíncronas", "2 sincrónicas", 
                                   "2 sincrónicas"]}))
    with total4:
        st.info('Inversión')
        st.write (pd.DataFrame({'Modalidad': ['General',
                                          'Estudiantes', 
                                          'Corporativo (grupos de 4)'], 
                                'Inversión': ["200", "150", 
                                           "160"]}))
    image = Image.open("logPann_red.png")
    st.image(image, caption='Redes Neuronales Artificiales')


##
st.header('Nuestras redes', divider='rainbow')

st.link_button("Youtube", "https://www.youtube.com/channel/UCm6lcnfmNS2stsUYVvrFOzg")

st.link_button("Facebook", "https://www.facebook.com/tallerespuquna")

st.link_button("Github", "https://github.com/inefable12")

image = Image.open("verano2023a.png")
st.image(image, caption='Puquna: Talleres STEAM')


##
page_names_to_funcs = {
  "Inicio": El_principito,
  "Cursos": page2,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
