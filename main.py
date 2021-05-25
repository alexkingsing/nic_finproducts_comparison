import pandas as pd
import streamlit as st
from utils import *

#configs
st.set_page_config(layout = "wide")

# begins here

st.title("La Magia del interés compuesto")
st.sidebar.title("Escoge como seguir!")
option = st.sidebar.radio("", page_options, index = 0)



if option == page_options[0]: #INTRODUCTION SECTION __COMPLETED__
    st.header("Bienvenid@! \U0001F44B") # Unicode escape character needed for Emoji

    st.write('''Este proyecto que nace del deseo de mejorar la educación financiera de la población Nicaraguense (o hispanohablante en general) en materia de inversiones. 
    Una de las más potentes (y relativamente simple) formas de hacer crecer tú dinero es invirtiendolo en productos financieros! Existen muchos (Depósitos, acciones, ETFs, Fondos Mutuos, etc
    que no son el foco de este proyecto. Acá nos centraremos en productos comúnes, simples, pero igualmente para potentes!  

    \n Esperamos que luego de usar esta herramienta puedas comprender mucho mejor como puedes usar las inversiones y el interés para hacer creer tu dinero!, 
    o si ya tienes conocimento puedes usar la herramienta para experimentar con tus futuras ganancias.

    \n Este es un proyecto conjunto entre **Elaine Miranda** CEO de https://plataconplatica.com/ y **Alexander King Sing** https://www.linkedin.com/in/alexanderkingsing/!''')

    st.subheader("Para empezar!")

    st.write(f"Puedes aprender sobre interés en la sección **Educativa** o si solo quieres calcular tus ganancias puedes usar la opción de **{page_options[2]}**.")

elif option == page_options[1]: #EDUCATIONAL SECTION __WILL BE DONE AT THE END__
    st.header("Bienvenid@ a la sección educativa! \U0001F913 \U0001F4D6")

    st.write('''
    Esta sección esta orientada a proporcionar información sobre interés compuesto y como funciona, y sobretodo, porque es tan potente! \n 
    Sin más preámbulo, empecemos!''')

    st.subheader("¿Qué es el interés?")


    st.subheader("Interés Simple vs Interés Compuesto")


elif option == page_options[2]: #CALCULATIONS

    st.subheader("Escoge la configuración para hacer tu comparación de productos!")
    st.write("Las opciones apareceran en la barra de la izquierda!")

    # Config params
    ### Interest rates / returns
    ir_save = st.sidebar.number_input("Tasa de interés de Cuenta de Ahorro", min_value = 0.0, value = 1.0, step = 0.1, key = "save") / 100
    ir_deposit = st.sidebar.number_input("Tasa de interés de Certificado de depósito", min_value = 0.0, value = 3.0, step = 0.1, key = "deposit") / 100
    ir_stock = st.sidebar.number_input("Retorno anual de la Bolsa de Valores", min_value = 0.0, value = 5.0, step = 0.1, key = "stock") / 100

    ### General params
    capitalization = st.sidebar.selectbox("Periodo de capitalización (cada cuanto ganas interés! mismo para todos los productos)", capitalization_periods, index = 3)
    capitalization = contribution_periods_val[capitalization]           
    years = st.sidebar.number_input("Por cuantos AÑOS deseas invertir este dinero?", min_value = 1, value = 5, step = 1)   
    multiple = st.sidebar.radio("Antes que todo, decide si prefieres ver la evolución de una única inversión o de varios aportes!", 
                ["Contribución única", "Múltiples contribuciones"], 
                index = 0)
    if multiple == "Contribución única":
        multiple = False
        contr_val = st.sidebar.number_input('''Inversión inicial''', value = 1000, step = 100)
    else:
        multiple = True
        contr_val = st.sidebar.number_input('''Aporte anual en USD.
        Se aportará lo mismo independiente de las diferencias en vencimientos de los productos financieros.''', 
        value = 1000, step = 100)

    ### PENDING ___ MAKE FUNCTION FOR ARRAY MAKE ____

    last_row = np.full((3,1), contr_val) ## CREATING THE INITIAL CONSTRUCTOR 2-D ARRAY BASED ON FINANCING OPTIONS. THIS WILL BE OVERWRITTEN AT THE LOOP.
    final_array = None

    for year in range(1 , (years + 1)):
        next_row = np.apply_along_axis(row_cal, 0, last_row, ir_save, ir_deposit, ir_stock, capitalization, multi = multiple) # calculating next
        
        if year == 1: #first item is a bit different
            final_array = np.concatenate((last_row, next_row), axis = 1)
            last_row = next_row
        else:
            final_array = np.concatenate((final_array, next_row), axis = 1)
            last_row = next_row

    df = pd.DataFrame(final_array.T, columns = fin_prod_list, dtype = "float")

    ### PLOT

    fig = plot_data(df)
    st.plotly_chart(fig, use_container_width = True)
    st.write(df.style.set_precision(2))
