import plotly.graph_objects as go
import numpy as np
import pandas as pd

#useful lists and parameters
page_options = ["Intro", "Educativo", "Calculo int. compuesto"]
contribution_periods = ["Quincenal", "Mensual", "Trimestral", "Bianual", "Anual"]
contribution_periods_val = {"Quincenal": 1/52,
                            "Mensual": 1/12,
                            "Trimestral": 1/4,
                            "Bianual": 1/2,
                            "Anual": 1}

capitalization_periods = ["Mensual", "Trimestral", "Bianual", "Anual"]
fin_prod_list = ["Cuenta", "Depósito", "Bolsa"]

##### FUNCTIONS ##################

def row_cal(array, ir_save, ir_deposit, ir_stock, capitalization, multi = True):
    '''calculates the next row of a numpy array based on the input array and pre-specified parameters
    
    RETURNS an array with the same shape as the parent array with new values    '''

    # environment variables of the function for cleaner read

    interest_save = 1 + (ir_save * capitalization)
    interest_deposit = 1 + (ir_deposit * capitalization)
    interest_stock = 1 + (ir_stock * capitalization)

    power = 1 / capitalization
    
    if multi == True:
    
        return ((array[0] * (interest_save ** power)) + 1000, 
        (array[1] * (interest_deposit ** power)) + 1000, 
        (array[2] * (interest_stock ** power)) + 1000) 
        # add previous value + gained interest per the period + contri
    
    else:
        return (array[0] * (interest_save ** power), 
        array[1] * (interest_deposit ** power), 
        array[2] * (interest_stock ** power)) 
        # add previous value + gained interest per the period

def plot_data(df):

    data = df
    columns = list(data.columns)

    x_ax = df.index

    fig = go.Figure()

    for i, column in enumerate(columns):
        fig.add_trace(go.Scatter(
            x = x_ax,
            y = data.iloc[:,i],
            mode = "lines",
            name = column)
        )

    fig.update_layout(legend = dict(
            yanchor = "top",
            y = 0.99,
            xanchor = "left",
            x = 0.01,
            bgcolor = "Azure"
        )
    )

    return fig

def sample_plot() -> any:

    val = 1000 # default value
    base_simp = [] # placeholder list for simple interest build
    base_comp = [] #placeholder list for compound interest build

    for i in range(0,30):
        base_simp.append( 50 * (i))
        base_comp.append(val * ((1.05)**i))

    base_comp = np.array(base_comp)
    base_comp = base_comp - val
    base_comp = base_comp.tolist()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
    x = list(range(0,30)),
    y = base_simp,
    mode = "lines + markers",
    name = "Interés simple acumulado",
    line = dict(color = "green"))
    )

    fig.add_trace(go.Scatter(
    x = list(range(0,30)),
    y = base_comp,
    mode = "lines + markers",
    name = "Interés compuesto acumulado")
    )

    return fig