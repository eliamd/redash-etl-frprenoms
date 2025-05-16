import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import os

# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname="data",
    user="useradmin",
    password="password",
    host="localhost",
    port="5433"
)

cur = conn.cursor()

# Recréation propre de la table
cur.execute("""
DROP TABLE IF EXISTS prenoms;
CREATE TABLE prenoms (
    sexe VARCHAR(1),
    prenom VARCHAR(255),
    annee INT,
    departement VARCHAR(5),
    nombre INT
);
""")

# Chargement du CSV
df = pd.read_csv("data/clean/data.csv")

# Conversion des lignes en tuples
data_tuples = list(df.itertuples(index=False, name=None))

print(f"⏳ Insertion de {len(data_tuples):,} lignes...")

# Insertion en bulk
execute_values(
    cur,
    "INSERT INTO prenoms (sexe, prenom, annee, departement, nombre) VALUES %s",
    data_tuples,
    page_size=10000  # Tu peux ajuster ce nombre
)

conn.commit()
cur.close()
conn.close()

print("✅ Insertion terminée avec succès.")
