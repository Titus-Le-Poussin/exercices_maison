import pandas as pd

LogData = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Log_Suspect\log.txt"

try:
    df = pd.read_csv(LogData, sep= ' - ', header = None, names = ['Date', 'ip'], engine = 'python')

    df_sorted = df.sort_values(by='ip', ascending=True)
    print(df_sorted)
    df_sorted_by_IP = df.groupby('ip').size()
    print("Nombre d'IP differentes :", len(df_sorted_by_IP))
    print("Voici le nombre de requetes par IP :")
    print(df_sorted_by_IP)
    print("Le/s log/s suspect est/sont:")
    print(df_sorted_by_IP[df_sorted_by_IP > 3])

except FileNotFoundError:
    print(f"Le fichier {LogData} n'a pas été trouvé.")