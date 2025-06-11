import pandas as pd

LogData = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Log_Suspect\log.txt"

try:
    df = pd.read_csv(LogData, sep= ' - ', header = None, names = ['Date', 'ip'], engine = 'python')

    df_sorted = df.sort_values(by='ip', ascending=True)
    print(df_sorted)


except FileNotFoundError:
    print(f"Le fichier {LogData} n'a pas été trouvé.")