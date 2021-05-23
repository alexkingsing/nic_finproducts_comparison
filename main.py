import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(layout= "wide")

st.title("La Magia del interés compuesto")


st.sidebar.title("Escoge como seguir!")
option = st.sidebar.radio("", ["Intro", "Educativo", "Educativo detallado", "Calculo"], index = 0)

if option == "Intro":
    pass


elif option == "Educativo":
    pass
    

elif option == "Educativo detallado":
    st.text(option)


elif option == "Calculo":
    st.text(option)


    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)


# constants used
val = 1000 # value of initial and recurrent investments

time_range = np.arange(1, 10) # setting the range from 1 to N for puro

product_list = ["Cuenta de Ahorro", "Certificado de Depósitos", "Bolsa de Valores"]


# range_val = val * (1+ir)**time_range
