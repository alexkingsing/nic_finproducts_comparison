from pandas.tseries.offsets import Tick
import plotly.graph_objects as go
import numpy as np
import pandas as pd

#useful lists and parameters
page_options = ["Intro", "Educativo", "Calculo int. compuesto"]
fin_prod_list = ["Cuenta", "Depósito", "Bolsa"]

##### FUNCTIONS ##################

def row_cal(array, ir_save, ir_deposit, ir_stock, contri, multi) -> np.array:
    '''calculates the next row of a numpy array based on the input array and pre-specified parameters
    
    RETURNS an array with the same shape as the parent array with new values    '''

    # environment variables of the function for cleaner read

    interest_save = 1 + ir_save 
    interest_deposit = 1 + ir_deposit
    interest_stock = 1 + ir_stock
    
    if multi == True:
    
        return ((array[0] * (interest_save)) + contri, 
        (array[1] * (interest_deposit)) + contri, 
        (array[2] * (interest_stock)) + contri) 
        # add previous value + gained interest per the period + contri
    
    else:
        return ((array[0] * interest_save), 
        (array[1] * interest_deposit), 
        (array[2] * interest_stock)) 

        # add previous value + gained interest per the period

def plot_data(df : pd.DataFrame) -> go.Figure:

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
            bgcolor = "Azure"),
        xaxis = dict(
            tickmode = "linear",
            tick0 = 0,
            dtick = 1),
        xaxis_title = "Años",
        yaxis_title = "Dólares"
    )

    return fig

def sample_plot() -> any:

    val = 1000 # default value
    base_simp = [] # placeholder list for simple interest build
    base_comp = [] #placeholder list for compound interest build

    for i in range(0,30):
        base_simp.append(50 * (i))
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