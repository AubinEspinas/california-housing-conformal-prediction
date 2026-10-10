def clean_data(df_house):
    df_house = df_house.copy()

    df_house = df_house[(df_house["AveRooms"] >= 1) & (df_house["AveOccup"] >= 1)]

    df_house = df_house[df_house["AveOccup"] <= 20]
    df_house = df_house[df_house["AveRooms"] <= 20]

    return df_house.reset_index(drop=True)

import pandas as pd

def clean_data_iqr(df, k=1.5):
    columns = [c for c in df.columns if c not in ["Latitude", "Longitude"]]
    df_clean = df.copy()
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - k * IQR
        upper = Q3 + k * IQR
        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]
    return df_clean.reset_index(drop=True)