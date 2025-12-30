import pandas as pd
from datetime import datetime

#Lire le fichier CSV généré
file_name = "data/raw/sales_20251229.csv" 
df = pd.read_csv(file_name)

#Nettoyage
#Supprimer les lignes avec quantité négative 
df = df[df["quantity"]>=0]

#Supprimer les lignes avec prix <=0
df = df[df["price"]>0]

#Calcul du total_amount
df["total_amount"] = df["quantity"] * df["price"]

#Ajouter colonnes pour dimension date

df["date_id"] = pd.to_datetime(df["sale_date"])
df["day"] = df["date_id"].dt.day
df["mounth"] = df["date_id"].dt.month
df["year"]  = df["date_id"].dt.year
df["week"] = df["date_id"].dt.isocalendar().week

# Sauvegarder dans processed/

df.to_csv("data/processed/sales_processed.csv", index = False)

print("Données nettoyées et enrichies sauvegardées dans data/processed")

