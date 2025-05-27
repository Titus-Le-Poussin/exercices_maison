import pandas as pd



file_path = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Analyse_ton_supermarché\ventes.csv"

try:
    df = pd.read_csv(file_path)
    print(df.head())
except FileNotFoundError:
    print(f"Le fichier {file_path} n'a pas été trouvé.")