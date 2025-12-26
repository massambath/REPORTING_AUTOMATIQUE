import pandas as pd
import _mysql_connector
from datetime import datetime

#----Paramètres MYSQL----

conn =  _mysql_connector.connect(
    host = 'localhost',
    user = "root",
    password =  "passer",
    database ="shop"
)
cursor = conn.cursor()

#----Charger le CSV transformé-----

file_name = "data/processed/sales_processed.csv"
df= pd.read_csv(file_name)


#---- Insert dans dim_product------

products = df[['product_name','category','price']].drop_duplicates()
for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO dim_product (product_name, category, price)
        VALUES (%s,%s,%s)
        ON DUPLICATE KEY UPDATE category=%s; price=%s     
                  """ )
