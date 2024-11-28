import pandas as pd
def load_data():
    """
    Load EV sales and charging points data from IEA API.

    The function makes two API calls to the IEA API to load historical EV sales and charging points data, and returns two Pandas DataFrames, one for each dataset. The returned DataFrames are filtered to only include the EV sales data.

    Returns:
        df_sales (pd.DataFrame): EV sales data
        df_charge (pd.DataFrame): EV charging points data
    """
    df_sales = pd.read_csv("https://api.iea.org/evs?parameters=EVsales&category=Historical&mode=Cars&csv=true")
    df_charge = pd.read_csv("https://api.iea.org/evs?parameters=EVchargingpoints&category=Historical&mode=EV&csv=true")
    df_sales = df_sales[df_sales.parameter == "EV sales"]
    
    return df_sales, df_charge

