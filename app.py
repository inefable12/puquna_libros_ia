import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

##############
st.sidebar.image("stabledifussion777.png",
                 caption="Portada creada con IA")

##############Pagina 1##############
def Home():
    st.markdown("# Juega a crear nuevas historias")
    #st.markdown("<h1 style='text-align: center; color: red;'>Juega a crear nuevas historias</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("# El principito en Machupichu")
    image = Image.open("elprincipito.jpeg")
    st.image(image, caption='El principito en Machupichu')

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('El principito ilustrado por ia')
        st.write('''Te imaginas al principito en nuevos escenarios, ¡por ejemplo en Machupichu! qué nuevas historias puede despertar nuestro imaginario a través de la generación de imágenes usando inteligencia artificial.''')
        
    with total2:
        st.info('Pedidos a inefable12@gmail o 957787559')
        st.write (pd.DataFrame({'Tipo': ['Físico, Tapa dura',
                                          'Físico, Tapa blanda', 
                                          'Digital'], 
                                'Inicio': ["S/ 60.00", "S/ 40.00", 
                                           "S/ 20.00"]}))
    image = Image.open("DALL·E 2022-12-26 21.10.51 - Humberto Maturana head for 3D printing.png")
    st.image(image, caption='Personaje ilustrado por IA para impresión 3D')
    
##############Pagina 2##############
def page2():
    st.markdown("# Tus propios libros ilustrados por ia")
    st.sidebar.markdown("# Mis creaciones")
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Curso virtual (8 horas)')
        st.write('''En nuestros talleres podrás aprender desde cero, 
        no requieres saber programar ya que hemos preparado plantillas con códigos
        listos para que puedas desplegar toda tu creatividad.''')
        st.write (pd.DataFrame({'Temas': ['Python y redes neuronales artificiales',
                                  'Procesamiento de Lenguaje Natural', 
                                  'Llama 2 y ChatGPT','IA generadora de imágenes'], 
                        'Horas': ["2", "2", 
                                   "2", "2"]}))
        st.write('No requieres instalar en tu computadora los programas empleados y el uso de estos son gratuitos de forma permanente.')
    with total4:
        st.info('Medios de Pago')
        st.write('''Puedes yapear al número 957787559 o depositar a:''')
        st.write('''Cuenta Simple Soles en Interbank es: 0463101896728.''') 
        st.write('''Cuenta Interbancaria (CCI) en Interbank es: 00304601310189672804.''')
        st.write('''Envía el recibo de pago a inefable12@gmail.com''')
        st.write (pd.DataFrame({'Modalidad': ['General',
                                          'Estudiantes', 
                                          'Corporativo (grupos de 4)'], 
                                'Inversión': ["S/ 200", "S/ 150", 
                                           "S/ 160"]}))
    image = Image.open("alberteinstein.jpeg")
    st.image(image, caption='¿Recuerdas cuando Albert Einstein visitó Machupichu? Despierta historias alucinantes a través de la generación de imágenes con IA.')
  
    image = Image.open("logPann_red.png")
    st.image(image, caption='Descubre cómo las redes neuronales artificiales están revolucionando diversas áreas del conocimiento')


##
def page3():
  st.header('Nuestras redes', divider='rainbow')
  
  st.link_button("Youtube", "https://www.youtube.com/channel/UCm6lcnfmNS2stsUYVvrFOzg")
  
  st.link_button("Facebook", "https://www.facebook.com/tallerespuquna")
  
  st.link_button("Github", "https://github.com/inefable12")
  
  image = Image.open("verano2023a.png")
  st.image(image, caption='Puquna STEAM')

  st.write('''Somos un emprendimiento enfocado en la aplicación de tecnologías para la educación. 
  Puquna promueve las metodologías STEAM a través de talleres gratuitos en zonas vulnerables y autogestiona actividades para su sostenimiento, como minicursos, seminarios, cursos virtuales en centros culturales, institutos y universidades. 
  Somos especialistas en inteligencia artificial, ciencia de datos, música algorítmica y arte disruptivo, simulaciones moleculares, 
  prototipado con impresión 3D, corte laser, y mucho más.''')

  #st.write('''Puquna STEAM - 2024''')
  st.markdown("<h1 style='text-align: center; color: purple;'>Puquna STEAM - 2024</h1>", unsafe_allow_html=True)

##
page_names_to_funcs = {
  "El principito": Home,
  "Cursos": page2,
  "Nuestras redes": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
