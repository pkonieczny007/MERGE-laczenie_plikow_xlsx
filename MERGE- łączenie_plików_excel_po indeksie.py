import pandas as pd
import os

# Wczytanie danych z pliku wykaz.xlsx
wykaz_df = pd.read_excel("wykaz.xlsx")

# Wczytanie danych z pliku roboczy_blachy.xlsx
blachy_df = pd.read_excel("roboczy_blachy.xlsx")

# Wczytanie danych z pliku roboczy_profile.xlsx
profile_df = pd.read_excel("roboczy_profile.xlsx")

# Połączenie danych na podstawie kolumny "Nr rys"
zlozenie_df = pd.merge(wykaz_df, blachy_df, how='left', on='Nr rys')
zlozenie_df = pd.merge(zlozenie_df, profile_df, how='left', on='Nr rys')

# Zapisanie wyników do pliku zlozenie.xlsx
zlozenie_df.to_excel("zlozenie.xlsx", index=False)
