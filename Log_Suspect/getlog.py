import pandas as pd
from datetime import datetime

LogData = r"C:\Users\Utilisateur\Documents\Informatique Etudes 2025\exercice\exo_maison\Log_Suspect\log.txt"

try:
    df = pd.read_csv(LogData, sep= ' - ', header = None, names = ['Date', 'ip'], engine = 'python')
    df['Date'] = pd.to_datetime(df['Date'])


    df_sorted = df.sort_values(by='ip', ascending=True)
    df_sorted_by_IP = df.groupby('ip').size()
    print("Nombre d'IP differentes :", len(df_sorted_by_IP))
    print("Voici le nombre de requetes par IP :")
    print(df_sorted_by_IP)

    suspects = []
    for ip in df_sorted_by_IP.index:
        dates = df[df['ip'] == ip]['Date'].sort_values().tolist()
        for i in range(len(dates) - 4):
            if (dates[i + 4] - dates[i]).total_seconds() < 300:
                suspects.append(ip)
                break
    if suspects:
        print("IP suspectes (5 requetes en moins de 5 minutes) :", suspects)
    else:
        print("Aucune IP suspecte trouvee.")

except FileNotFoundError:
    print(f"Le fichier {LogData} n'a pas été trouvé.")