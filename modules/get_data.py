import pandas as pd
from jh_utils.data.pandas.preprocessing import make_dummies

def get_data(first_columns = 6):
    return pd.read_csv('asteroides/asteoides.csv').iloc[:,first_columns:]

def transform_dummies(df):
    df.neo = make_dummies(df.neo)
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
    df = drop_bad_columns(df)
    return transform_dummies(df)

def get_x_y_no_NaNs():
    df = get_clean_data_for_ml()

    now_NaN_columns = ["neo","tp_cal",
    "tp","class",
    "w","om","i","q","a","e",
    "n","epoch_cal","epoch_mjd","epoch","pha"]

    #ret = pd.concat([df,make_dummies(df['class'])],axis=1)
    ret = df[now_NaN_columns]
    ret = ret[ret['pha'].notna()]

    y = ret['pha']
    x = ret.drop(['pha'],axis=1)
    
    return x,y 

## for later
def get_x_y():
    df = get_clean_data_for_ml()
    columns = ['pha','ma','per','per_y','rms','H']
    for i in columns:
        df = df[df[i].notna()]

    y = df['pha']
    x = df.drop('pha',axis=1)
    return x,y 
