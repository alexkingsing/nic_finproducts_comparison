import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

#useful lists and parameters
page_options = ["Intro", "Educativo", "Calculo (Contribución única)", "Calculo (Contribución períodica)"]
contribution_periods = ["Quincenal", "Mensual", "Trimestral", "Bianual", "Anual"]
contribution_periods_val = {"Quincenal": 1/52,
                            "Mensual": 1/12,
                            "Trimestral": 1/4,
                            "Bianual": 1/2,
                            "Anual": 1}
capitalization_periods = ["Mensual", "Trimestral", "Bianual", "Anual"]

# functions
def row_cal(array, ir_save, ir_deposit, ir_stock, capi_save, capi_deposit, capi_stock, multi = True):
    '''calculates the next row of a numpy array based on the input array and pre-specified parameters
    returns an array with the same shape as the parent array'''

    if multi == True:
        return ((array[0] * (1 + ir_save)) + 1000, (array[1] * (1+ir_deposit)) + 1000, (array[2] * (1+ir_stock)) + 1000) # add previous value + gained interest per the period + contri
    else:
        return (array[0] * (1 + ir_save), array[1] * (1+ir_deposit), array[2] * (1+ir_stock)) # add previous value + gained interest per the period


#configs
st.set_page_config(layout= "wide")


# begins here

st.title("La Magia del interés compuesto")
st.sidebar.title("Escoge como seguir!")
option = st.sidebar.radio("", page_options, index = 0)


if option == page_options[0]: #INTRODUCTION SECTION __COMPLETED__
    st.header("Bienvenid@! \U0001F44B") # Unicode escape character needed for Emoji

    st.write('''Este proyecto que nace del deseo de mejorar la educación financiera de la población Nicaraguense (o hispanohablante en general) en materia de inversiones. 
    Una de las más potentes (y relativamente simple) formas de hacer crecer tú dinero es invirtiendolo en productos financieros! Existen muchos (Depósitos, acciones, ETFs, Fondos Mutuos, etc
    que no son el foco de este proyecto. Acá nos centraremos en productos comúnes, simples, pero igualmente para potentes!  

    \n\n Esperamos que luego de usar esta herramienta puedas comprender mucho mejor como puedes usar las inversiones y el interés para hacer creer tu dinero!, 
    o si ya tienes conocimento puedes usar la herramienta para experimentar con tus futuras ganancias!''')
    
    st.write('''Este es un proyecto conjunto entre **Elaine Miranda** CEO de https://plataconplatica.com/ y **Alexander King Sing** https://www.linkedin.com/in/alexanderkingsing/''')

    st.subheader("Para empezar!")

    st.write("Puedes aprender sobre interés en la sección **Educativa** o si solo quieres calcular tus ganancias puedes usar las opciones en la barra de la izquierda.")
    st.write(f" **{page_options[2]}** es para cálcular tus ganancias a futuro con una inversión ÚNICA (sin aportes a futuro)")
    st.write(f" **{page_options[3]}** es para cálcular tus ganancias a futuro con aportes recurrentes")

elif option == page_options[1]: #EDUCATIONAL SECTION __WILL BE DONE AT THE END__
    st.header("Bienvenid@ a la sección educativa! \U0001F913 \U0001F4D6")

    st.write('''
    Esta sección esta orientada a proporcionar información sobre interés compuesto y como funciona, y sobretodo, porque es tan potente! \n 
    Sin más preámbulo, empecemos!''')

    st.subheader("¿Qué es el interés?")


    st.subheader("Interés Simple vs Interés Compuesto")


elif option == page_options[2]: #CALCULATIONS (FORM 1)
    st.subheader("Escoge la configuración para hacer tu comparación de productos!")

    with st.form("form1"):
        
        col1, col2, col3, col4 = st.beta_columns(4)
        
        with col1: # COLUMN FOR SAVINGS ACCOUNT
            st.write("Cuenta de Ahorro")
            ir_save = st.number_input("Tasa de interés anual", min_value = 0, value = 5, step = 1, key = "save") / 100
            capi_save = st.selectbox("Periodo de capitalización (cada cuanto ganas interés!)", capitalization_periods, index = 3, key = "save")

        with col2: # COLUMN FOR CERTIFICATE DEPOSIT CALCULATION
            st.write("Certificado de depósito")
            ir_deposit = st.number_input("Tasa de interés anual", min_value = 0, value = 5, step = 1, key = "deposit") / 100
            capi_deposit = st.selectbox("Periodo de capitalización (cada cuanto ganas interés!)", capitalization_periods, index = 3, key = "deposit")

        with col3: # COLUMN FOR STOCK CONTRIBUTION
            st.write("Bolsa de Valores")
            ir_stock = st.number_input("Tasa de interés anual", min_value = 0, value = 5, step = 1, key = "stock") / 100
            capi_stock = st.selectbox("Periodo de capitalización (cada cuanto ganas interés!)", capitalization_periods, index = 3, key = "stock")

        with col4: # COLUMN FOR VALUE AND CONTRIBUTION CONFIG
            st.write("Valor a aportar (USD)")
            
            contr_val = st.number_input("Puede escribirlo directamente o usar los botones para sumar/restar de 100 en 100", value = 1000, step = 100)

        submitted = st.form_submit_button("Vamos!!")

    if submitted == True:
        st.write(F"SUCCESS {ir_save}")

        first_row = np.full(3, contr_val)
        second_row = np.apply_along_axis(row_cal, 0, first_row, ir_save, ir_deposit, ir_stock, capi_save, capi_deposit, capi_stock, multi = True)

        st.write(first_row)
        st.write(second_row)

elif option == page_options[3]: #CALCULATIONS (FORM 1)

    st.subheader("Escoge la configuración para hacer tu comparación de productos!")

    with st.form("my_form"): # creating configuration panel through form for easier capture and processing

        col1, col2, col3, col4 = st.beta_columns(4)
        
        with col1: # COLUMN FOR SAVINGS ACCOUNT
            st.write("Cuenta de Ahorro")

        with col2: # COLUMN FOR CERTIFICATE DEPOSIT CALCULATION
            st.write("Certificado de depósito")

        with col3: # COLUMN FOR STOCK CONTRIBUTION
            st.write("Bolsa de Valores")
        
        with col4: # COLUMN FOR VALUE AND CONTRIBUTION CONFIG
            st.write("Valor a aportar (USD)")
            
            contr_val = st.number_input("Puede escribirlo directamente o usar los botones para sumar/restar de 100 en 100", value = 1000, step = 100)
            
            contr_period = st.selectbox("Frecuencia de contribucion (para productos con vencimiento mayor a la contribucion, la contribucion se acumulara y se aplicara al principal al vencimiento", contribution_periods, index = len(contribution_periods) - 1 )
            contr_period_val = contribution_periods_val[contr_period]

        submitted = st.form_submit_button("Aplicar") # Every form must have a submit button. This returns a boolean that can be used for further customization.

    if submitted == True:
        st.write(f"CORRECTLY EXECUTED: contribucion = {contr_val}, periodo = {contr_period_val}")