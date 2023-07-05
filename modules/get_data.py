import pandas as pd
from jh_utils.data.pandas.preprocessing import make_dummies

def get_data(first_columns = 6):
    return pd.read_csv('asteroides/asteoides.csv').iloc[:,first_columns:]

def transform_dummies(df):
    df.neo = make_dummies(df.neo)
    df.pha = make_dummies(df.pha)
    return df

def drop_bad_columns(df):
    columns_to_drop = ['orbit_id',
                       'diameter',
                       'diameter_sigma',
                       'albedo',
                       'equinox']
    return df.drop(columns_to_drop,axis=1)

def get_clean_data_for_ml():
    df = get_data()
    df = transform_dummies(df)
    df = drop_bad_columns(df)
    return df

def get_x_y():
    df = get_clean_data_for_ml()
    y = df['class']
    x = df.drop('class',axis=1)
    return x,y 

