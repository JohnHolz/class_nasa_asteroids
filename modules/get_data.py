import pandas as pd
from jh_utils.data.pandas.preprocessing import make_dummies


def get_data(first_columns=6):
    return pd.read_csv("asteroides/asteoides.csv").iloc[:, first_columns:]


def transform_dummies(df):
    df.neo = make_dummies(df.neo)
    return df


def drop_bad_columns(df):
    columns_to_drop = ["orbit_id", "diameter", "diameter_sigma", "albedo", "equinox"]
    return df.drop(columns_to_drop, axis=1)


def get_clean_data_for_ml():
    df = get_data()
    df = drop_bad_columns(df)
    return transform_dummies(df)


def get_x_y(as_numpy=False):
    df = get_clean_data_for_ml()
    columns = ["pha", "ma", "per", "rms", "H"]
    columns_linear_depen = ["epoch_mjd", "epoch_cal", "tp_cal", "per_y", "moid_ld"]
    df.drop(columns_linear_depen, axis=1, inplace=True)

    for i in columns:
        df = df[df[i].notna()]

    ## the bad steps
    y = df["pha"]
    y = make_dummies(y)
    x = df.drop("pha", axis=1)
    x = pd.concat([x, make_dummies(x["class"])], axis=1)
    x.drop("class", axis=1, inplace=True)

    if as_numpy == True:
        return x.to_numpy(), y.to_numpy()

    return x, y
    ## to return numpy array use .to_numpy()


# def get_x_y():
#     df = get_clean_data_for_ml()
#     columns = ['pha','ma','per','per_y','rms','H']
#     for i in columns:
#         df = df[df[i].notna()]

#     y = df['pha']
#     x = df.drop('pha',axis=1)
#     return x,y
