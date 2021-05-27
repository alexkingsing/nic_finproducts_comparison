import numpy as np
import pandas as pd
import streamlit as st
from utils import *
import edu

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

    st.write(edu.intro)

    st.markdown(edu.index)

    st.subheader("1. ¿Qué es el interés?")

    st.write(edu.interest)
    st.latex("I = R + In + Op")
    st.write('''Listo! Hay mucho más que decir sobre interés, pero esperamos que esta introducción haya sido de su agrado. 
    A continuación hablaremos de los 2 principales tipos de interés.''')
    st.markdown("***") ## Section separator.

    st.subheader("2. Tipos de interés")

    st.write(edu.interest_types)
    st.markdown("***") ## Section separator.

    st.subheader(" 3.Interés Simple vs Interés Compuesto")

    st.write(edu.interest_simvscomp)
    st.markdown("***") ## Section separator.

elif option == page_options[2]: #CALCULATIONS

    st.subheader("Escoge la configuración para hacer tu comparación de productos!")
    
    with st.beta_expander("Click AQUI para esconder las opciones de configuración!", expanded = True): # CONFIG OPTIONS SECTION.

        with st.form("form"):
            
            col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
            
            with col1:
                ir_save = st.number_input("Interés anual de Cuenta de Ahorros", min_value = 0.0, value = 1.0, step = 0.1, key = "save") / 100
            
            with col2:
                ir_deposit = st.number_input("Interés anual de Cert. de depósito", min_value = 0.0, value = 3.0, step = 0.1, key = "deposit") / 100
            
            with col3:
                ir_stock = st.number_input("Retorno anual de la Bolsa de Valores", min_value = 0.0, value = 5.0, step = 0.1, key = "stock") / 100

            with col4:
                capitalization = st.selectbox("Periodo de capitalización (cada cuanto ganas interés!)", capitalization_periods, index = 3)
                capitalization = contribution_periods_val[capitalization]           
            
            with col5:
                years = st.number_input("Por cuantos AÑOS deseas invertir este dinero?", min_value = 1, value = 3, step = 1)
            
            with col6:
                multiple = st.radio("Decide si prefieres ver la evolución de una única inversión o de varios aportes!", 
                            ["Contribución única", "Múltiples contribuciones"], 
                            index = 0)
            if multiple == "Contribución única":
                multiple = False
                contr_val = st.number_input('''Inversión inicial''', value = 1000, step = 100)
            else:
                multiple = True
                contr_val = st.number_input('''Aporte anual en USD.
                Se aportará lo mismo independiente de las diferencias en vencimientos de los productos financieros.''', 
                value = 1000, step = 100)

            submitted = st.form_submit_button("Vamos!!")
            st.caption("Dar click acá cada vez que actualices data!")

    if submitted == True:
        last_row = np.full((3, 1), contr_val) ## CREATING THE INITIAL CONSTRUCTOR 2-D ARRAY BASED ON FINANCING OPTIONS. THIS WILL BE OVERWRITTEN AT THE LOOP.
        final_array = None

        for year in range(1, (years + 1)):
            next_row = np.apply_along_axis(row_cal, 0, last_row, ir_save, ir_deposit, ir_stock, capitalization, multi = multiple) # calculating next
            
            if year == 1: #first item is a bit different
                final_array = np.concatenate((last_row, next_row), axis = 1)
                last_row = next_row
            else:
                final_array = np.concatenate((final_array, next_row), axis = 1)
                last_row = next_row

        df = pd.DataFrame(final_array.T, columns = fin_prod_list, dtype = "float")

        ### PLOT AND TABLES SECTION ###
        col_1, col_2 = st.beta_columns([4,1])

        with col_1:
            fig = plot_data(df)
            st.plotly_chart(fig, use_container_width = True)
            
        with col_2:
            
            sum_df = df.iloc[-1,:].sort_values(ascending=False)

            st.write("Los retornos en el último año son:")

            st.table(sum_df)

            dif = (sum_df.max() - sum_df.min())

            st.write(f"La diferencia entre el máximo y el mínimo a los **{years} años** es de: **{dif:.2f}** USD")