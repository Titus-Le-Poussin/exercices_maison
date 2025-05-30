import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


Dataframe = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Analyse_ton_supermarché\ventes.csv"

try:
    df = pd.read_csv(Dataframe)

    # Consigne: Afficher le prix total de tous les produits

    df["CA"] = df["Quantite"] * df["Prix_unitaire"]
    df_all_price = df["CA"].sum()

    df_trie_price = df.sort_values(by='Prix_unitaire', ascending=False)

    # Consigne : Afficher le produit le plus vendu par quantité
    df_trie_quantity = df.sort_values(by='Quantite', ascending=False)

    # Consigne: Afficher le jour avec le plus de ventes
    df_trie_date = df.sort_values(by='CA', ascending=False)

    # Consigne : Afficher le chiffre d'affaire par catégorie
    df_trie_category = df.sort_values(by='Categorie', ascending=True)
    df_price_category = df.groupby('Categorie')['CA'].sum().reset_index()
    

    # les prints
    print(df.head(12))
    print("il y a", len(df), "produits en tout")
    print("Voici le produit le plus cher :", df_trie_price.iloc[0]["Produit"])
    print("Voici le jour avec le plus de ventes : ", df_trie_date.iloc[0]["Date"], "avec le produit", df_trie_date.iloc[0]["Produit"])
    print("Voici le produit le plus vendu:", df_trie_quantity.iloc[0]["Produit"], "avec une quantite de", df_trie_quantity.iloc[0]["Quantite"])
    print("Voici le chiffre d'affaire par categorie :")
    print(df_price_category)


    print("Le prix total de tous les produits est :", df_all_price)



    plt.figure(figsize=(10, 6))
    plt.title("Ventes du supermarché")
    plt.xlabel("Date")
    plt.ylabel("Chiffre d'Affaires")
    plt.grid(axis='y')
    date_formatter = DateFormatter("%d/%m/%Y")
    plt.gca().xaxis.set_major_formatter(date_formatter)
    plt.xticks(rotation=45)
    plt.bar(df_trie_date["Date"], df_trie_date["CA"], color='blue', label="Chiffre d'Affaires")
    plt.yticks(range(0, int(df_trie_date.max()) + 1))
    plt.bar(df_trie_date["Date"], df_trie_date["CA"], color='blue', label='Chiffre d\'Affaires')
    plt.legend()
    plt.show()
    plt.tight_layout()

except FileNotFoundError:
    print(f"Le fichier {Dataframe} n'a pas été trouvé.")