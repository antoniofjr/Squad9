import pandas as pd

def read_csv(path):

    try:
        return pd.read_csv(path)
    except:
        return None