import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


Dataframe = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Analyse_ton_supermarché\ventes.csv"

try:
    df = pd.read_csv(Dataframe)
    print(df)
    print("il y a", len(df), "produits en tout")
    df_trie = df.sort_values(by='Prix_unitaire', ascending=False)
    print("Voici les 5 produits les plus chers :")
    print(df_trie.head(5))
    df_prix = df["Prix_unitaire"] * df["Quantite"]
    print(df["Produit"], df_prix)
except FileNotFoundError:
    print(f"Le fichier {Dataframe} n'a pas été trouvé.")