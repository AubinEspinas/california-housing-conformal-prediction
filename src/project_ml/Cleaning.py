def clean_data(df_house):
    df_house = df_house.copy()

    df_house = df_house[(df_house["AveRooms"] >= 1) & (df_house["AveOccup"] >= 1)]

    df_house = df_house[df_house["AveOccup"] <= 20]
    df_house = df_house[df_house["AveRooms"] <= 20]

    return df_house.reset_index(drop=True)