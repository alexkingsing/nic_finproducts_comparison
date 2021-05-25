import numpy as np
import plotly.graph_objects as go

#useful lists and parameters
page_options = ["Intro", "Educativo", "Calculo"]
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

    return fig