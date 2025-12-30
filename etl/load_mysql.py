import pandas as pd
import mysql.connector
from datetime import datetime

# Connexion MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passer",
    database="shop"
)
cursor = conn.cursor()

# Charger le CSV transformé
df = pd.read_csv("data/processed/sales_processed.csv")

# -------- DIM PRODUCT --------
products = df[['product_name', 'category', 'price']].drop_duplicates()

for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO dim_product (product_name, category, price)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            category = VALUES(category),
            price = VALUES(price)
    """, (row['product_name'], row['category'], row['price']))

# -------- DIM DATE --------
dates = df['sale_date'].drop_duplicates()

for d in dates:
    dt = datetime.strptime(d, "%Y-%m-%d")
    # On n'insère pas date_id, MySQL le crée automatiquement
    cursor.execute("""
        INSERT INTO dim_date (date_id, day, month, year, week)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            day = VALUES(day),
            month = VALUES(month),
            year = VALUES(year),
            week = VALUES(week)
    """, (dt.date(), dt.day, dt.month, dt.year, dt.isocalendar()[1]))

# -------- FACT SALES --------
for _, row in df.iterrows():
    dt = datetime.strptime(row['sale_date'], "%Y-%m-%d")
    
    # Récupérer le date_id correspondant
    cursor.execute("SELECT date_id FROM dim_date WHERE date_id = %s", (dt.date(),))
    date_id = cursor.fetchone()[0]

    # Récupérer le product_id correspondant
    cursor.execute("SELECT product_id FROM dim_product WHERE product_name = %s", (row['product_name'],))
    product_id = cursor.fetchone()[0]

    # Insérer dans fact_sales
    cursor.execute("""
        INSERT INTO fact_sales (product_id, date_id, quantity, total_amount)
        VALUES (%s, %s, %s, %s)
    """, (
        product_id,
        date_id,
        row['quantity'],
        row['total_amount']
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Données chargées avec succès dans MySQL")
