import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Dossier pour les fichiers raw
os.makedirs("data/raw", exist_ok=True)

# Paramètres 
num_days = 90 #3mois
num_products = 20

products = [f"Product_{i+1}" for i in range(num_products)]
categories = ["Food","Beverage","Electronics","Clothing"]

# Génération des ventes

all_sales = []

start_date = datetime.today() - timedelta(days=num_days)


for i in range(num_days):
    current_date = start_date + timedelta(days = i)
    for product in products :
        # Quantité alératoire vendue
        quantity = random.choices([0,1,2,3,4,5,6,7,8,9,10], weights=[1,2,3,5,4,3,2,1,1,1,1])[0]
        # Prix aléatoire selon catégorie
        category = random.choice(categories)
        price = round(random.uniform(5,100),2)

        # Introduire des anomalies légères
        if random.random() < 0.02:
            quantity = -quantity #valeur négative incorrecte

        all_sales.append({
            "sale_date": current_date.strftime("%Y-%m-%d"),
            "product_name" : product,
            "category" : category,
            "quantity": quantity,
            "price": price
        })

# Créer le dataframe
df = pd.DataFrame(all_sales)

# sauvegarder CSV

file_name = f"data/raw/sales_{datetime.today().strftime('%Y%m%d')}.csv"
df.to_csv(file_name, index= False)

print(f"CSV généré : {file_name}")