import pandas as pd
import matplotlib.pyplot as plt



Dataframe = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Analyse_ton_supermarché\ventes.csv"

try:
    df = pd.read_csv(Dataframe)
    print(df.head())
    df["Total"] = df["Quantite"] * df["Prix Unitaire"]
except FileNotFoundError:
    print(f"Le fichier {Dataframe} n'a pas été trouvé.")