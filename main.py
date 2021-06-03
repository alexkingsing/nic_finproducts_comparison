import numpy as np
import pandas as pd
import streamlit as st
import edu
from utils import *

#configs
st.set_page_config(layout = "wide")

# begins here

st.title("El poder del interés compuesto")
st.sidebar.title("Escoge como seguir!")
option = st.sidebar.radio("", page_options, index = 0)

if option == page_options[0]: #INTRODUCTION SECTION __COMPLETED__
    st.header("Bienvenid@! \U0001F44B") # Unicode escape character needed for Emoji

    st.write('''Este proyecto que nace del deseo de mejorar la educación financiera de la población Nicaraguense (o hispanohablante en general) en materia de inversiones. 
    Una de las más potentes (y relativamente simple) formas de hacer crecer tú dinero es invirtiendolo en productos financieros! Existen muchos (Depósitos, acciones, ETFs, Fondos Mutuos, etc
    que no son el foco de este proyecto. Acá nos centraremos en productos comúnes, simples, pero igualmente potentes para multiplicar tú dinero! \U0001F4B8 \U0001F4B8 \U0001F4B8

    \n Esperamos que luego de usar esta herramienta puedas comprender mucho mejor como puedes usar las inversiones y el interés para hacer creer tu dinero!,
    o si ya tienes conocimento puedes usar la herramienta para experimentar con tus futuras ganancias.

    \n Este es un proyecto de **Alexander King Sing** \U0001F4CC https://www.linkedin.com/in/alexanderkingsing/! inspirado en el trabajo de **Elaine Miranda** CEO \U0001F4BC de https://plataconplatica.com/ 
    
    \n **DISCLAIMER**: Está aplicación **NO** constituye consejo de inversión.''')

    st.subheader("Para empezar!")

    st.write(f'''Puedes aprender sobre interés en la sección **{page_options[1]}** \U0001F4D6 
    o si solo quieres calcular tus ganancias puedes usar la opción de **{page_options[2]}** \U0001F4CA.
    \n Asimismo, algunas notes sobre el origen de los valores por defecto de la calculadora:
    \n * Los valores de interés / retorno por defecto de **cuentas de ahorro** fueron obtenidos en base a experiencia personal y no representan un compromiso legal u otro
    con ninguna entidad financiera en particular. Las tasas están sujetas a discreción de la entidad emisora + aspectos regulatorios. Por favor consultar con su banco.
    \n * Los valores de interés / retorno por defecto de **certificados de depósito** fueron obtenidos en base a experiencia personal con este producto y no representan un compromiso
    con ninguna entidad financiera en particular. Las tasas están sujetas a discreción de la entidad emisora + aspectos regulatorios. Por favor consultar con su banco.
    \n * Los valores de interés / retorno por defecto del **mercado de bolsa de valores** fueron obtenidos mediante investigación de fuentes oficiales y extrapolación personal.
    La información histórica (auditada) puede encontrarse en la página del Banco Central de Nicaragua:
    \n   * https://www.bcn.gob.ni/publicaciones/periodicidad/trimestral/valores/index.php
    \nSiempre por favor recordar: **Cualquier inversión tiene un RIESGO**. Si este riesgo es adecuado para el inversionista es un ejercicio **PERSONAL**.
    Si tiene dudas consulte con su banco, investigue más al respecto, o avoquése con un experto financiero!''')

elif option == page_options[1]: #EDUCATIONAL SECTION __COMPLETED__
    st.header("Bienvenid@ a la sección educativa! \U0001F913 \U0001F4D6")

    st.write(edu.intro)
    st.markdown(edu.index)

    st.subheader("1. ¿Qué es el interés? \U0001F4B1")
    st.write(edu.interest)
    st.latex("I = R + In + Op")
    st.write('''*Esto se lee*: "El interés es igual a: El riesgo (en porcentaje) + el porcentaje de inflación esperado + el costo de oportunidad (en porcentaje)
    \n Listo! Hay mucho más que decir sobre interés, pero esperamos que esta introducción haya sido de su agrado. 
    A continuación hablaremos de los 2 principales tipos de interés.''')
    st.markdown("***") ## Section separator.

    st.subheader("2. Tipos de interés \U0001F4B2")
    st.write(edu.interest_types_simple)
    st.latex(r"I = P * r ")
    st.write(edu.interest_types_simple_pt2)
    st.plotly_chart(simple_int_plot(), use_container_width=True)
    st.write("Dicho eso, es ahora de pasar al más interesante de ambos, el interés compuesto!")
    st.write(edu.interest_types_compound)
    st.latex(r'''
        V_f = P * (1 + {r \over n}) ^ {r \over n}
        ''')
    st.write(edu.interest_types_compound_pt2)
    st.latex(r'''
    V_f = P * ( 1 + r) ^ n
    ''')
    st.write(edu.interest_types_compound_pt3)
    st.plotly_chart(comp_int_plot(), use_container_width=True)
    st.write("¿Aún no te impresiona? pues ve en la próxima sección y mirarás el poder y la magia del interés compuesto!")
    st.markdown("***") ## Section separator.

    st.subheader("3. Interés Simple vs Interés Compuesto \U0001F4B0")
    st.write(edu.interest_simvscomp)
    st.plotly_chart(sample_plot(), use_container_width = True)
    st.write(edu.interest_simvscomp_pt2)
    st.markdown("***") ## Section separator.
    
    st.subheader("Anexo \U0001F913")
    st.write(edu.annex)
    st.latex(r"I = P * r  \qquad (1)")
    st.write(edu.annex_2)
    st.latex(r"V_f = P + (I)  \qquad (2)")
    st.write(edu.annex_3)
    st.latex(r"V_f = P + (P*r) \qquad Substituyendo \: (1) \: en \: (2)")
    st.latex(r"V_f = P * (1 + r) \qquad Agrupando \: obtenemos \: (3)")
    st.write(edu.annex_4)
    st.latex(r"V_f = P + I_0 + I_1 \qquad (4)") 
    st.write(edu.annex_5)
    st.latex(r"V_f = P + (P * r) + (P * (1 + r)) \qquad Substituyendo \: (1) \: y \: (3) \: en \: (4)")
    st.write(edu.annex_6)
    st.latex(r"V_f = P * (1 + r) * (1 * (1 + r)) \qquad Agrupando \: (P)")
    st.latex(r"V_f = P * (1 + r) * (1 + r) \qquad Simplificando")
    st.write(edu.annex_7)
    st.latex(r"V_f = P * (1+r)^2 \qquad Simplificando \: potencia")
    st.write(edu.annex_8)
    st.latex(r"V_f = P * ( 1 + r) ^ n \qquad Generalizando \: para \: todos \: los \: períodos \: n")
    st.write(edu.annex_9)

elif option == page_options[2]: #CALCULATIONS __COMPLETED__

    st.subheader("Escoge la configuración para hacer tu comparación de productos!")
    
    with st.beta_expander("Click AQUI para esconder las opciones de configuración!", expanded = True): # CONFIG OPTIONS SECTION.

        with st.form("form"):
            
            col1, col2, col3, col4, col5 = st.beta_columns(5)
            
            with col1:
                ir_save = st.number_input("Interés anual de Cuenta de Ahorros", min_value = 0.0, value = 1.0, step = 0.1, key = "save") / 100
            
            with col2:
                ir_deposit = st.number_input("Interés anual de Cert. de depósito", min_value = 0.0, value = 3.0, step = 0.1, key = "deposit") / 100
            
            with col3:
                ir_stock = st.number_input("Retorno anual de la Bolsa de Valores", min_value = 0.0, value = 5.0, step = 0.1, key = "stock") / 100

            with col4:
                periods = st.number_input("Por cuantos AÑOS deseas invertir este dinero?", min_value = 1, value = 10, step = 1)
            
            with col5:
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

            submitted = st.form_submit_button("Vamos!!") ## MANDATORY BOOLEAN OPTION
            st.caption("Dar click acá para iniciar o cada vez que actualices data!")

    if submitted == True:
        last_row = np.full((3, 1), contr_val) ## CREATING THE INITIAL CONSTRUCTOR 2-D ARRAY BASED ON FINANCING OPTIONS. THIS WILL BE OVERWRITTEN AT THE LOOP.
        final_array = None

        for year in range((periods)): # WE NEED +1 TO GET THE CORRECT LENGHT
            next_row = np.apply_along_axis(row_cal, 0, last_row, ir_save, ir_deposit, ir_stock, contr_val ,multi = multiple) # calculating next array to concat
            
            if year == 0: #first item is a bit different
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
            
            sum_df = df.iloc[-1,:].sort_values(ascending=False) # RETRIEVING ONLY LAST ROW OF EVERY COLUMN

            if multiple == True:
                st.write(f"Invertiste **{contr_val * periods} USD** en total. El valor de está inversión **al final de los {periods} años** es:")
            else:
                st.write(f"Invertiste **{contr_val} USD** en total. El valor de está inversión **al final de los {periods} años** es:")

            st.table(sum_df)

            dif = (sum_df.max() - sum_df.min()) 

            st.write(f'''La diferencia entre invertir en **{sum_df.index[sum_df.argmax()]}** (máximo)  o en **{sum_df.index[sum_df.argmin()]}** (mínimo) 
            a los **{periods} años** de invertir es de: **{dif:.2f}** USD''')
