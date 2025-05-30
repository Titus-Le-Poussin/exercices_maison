import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


Dataframe = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Analyse_ton_supermarché\ventes.csv"

try:
    df = pd.read_csv(Dataframe)

    df["Total"] = df["Quantite"] * df["Prix_unitaire"]
    df_all_price = df["Total"].sum()

    df_trie_price = df.sort_values(by='Prix_unitaire', ascending=False)
    df_trie_quantity = df.sort_values(by='Quantite', ascending=False)
    print(df)
    print("il y a", len(df), "produits en tout")
    print("Voici le produit le plus cher :", df_trie_price.iloc[0]["Produit"])
    print("Voici le produit le plus vendu:", df_trie_quantity.iloc[0]["Produit"], "avec une quantite de", df_trie_quantity.iloc[0]["Quantite"])
    print("Le prix total de tous les produits est :", df_all_price)
except FileNotFoundError:
    print(f"Le fichier {Dataframe} n'a pas été trouvé.")