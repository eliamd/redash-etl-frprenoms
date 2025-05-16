import os

import pandas as pd
import unidecode
from tqdm import tqdm

# Load raw file
df = pd.read_csv('../data/raw/dpt2022.csv', sep=';')

# ────────────────────────────────────── 1 : Sexe ──────────────────────────────────────

df['sexe'] = df['sexe'].replace({1: 'M', 2: 'F'})

# ──────────────────────────────────── 2 : Prénoms ─────────────────────────────────────

# Renommer la colonne 'preusuel' en 'prenom'
df = df.rename(columns={'preusuel': 'prenom'})
# Drop prénoms anonymes
df = df[df['prenom'] != '_PRENOMS_RARES']
# Mettre les prénoms en majuscules
df['prenom'] = df['prenom'].astype(str)

df['prenom'] = df['prenom'].apply(lambda x: unidecode.unidecode(x.upper()))


# ───────────────────────────────────── 3 : Années ─────────────────────────────────────

# Renommer la colonne 'annais' en 'annee'
df = df.rename(columns={'annais': 'annee'})

# Mettre les années XXXX en NaN
df['annee'] = pd.to_numeric(df['annee'], errors='coerce')
# Drop les lignes avec des années NaN
df = df.dropna(subset=['annee'])
# Convertir les années en entiers
df['annee'] = df['annee'].astype(int)

# Drop les lignes avec des années < 1900 ou > 2022
df = df[df['annee'] >= 1900]
df = df[df['annee'] <= 2022]

# ────────────────────────────────── 4 : Departement ───────────────────────────────────

df = df.rename(columns={'dpt': 'departement'})
#Mettre les XX en NaN
df['departement'] = pd.to_numeric(df['departement'], errors='coerce')
# Drop les lignes avec des départements NaN
df = df.dropna(subset=['departement'])
# Convertir les départements en entiers
df['departement'] = df['departement'].astype(int)

# ───────────────────────────────────── 5 : Nombre ─────────────────────────────────────

df['nombre'] = pd.to_numeric(df['nombre'], errors='coerce')
# Drop les lignes avec des nombres NaN
df = df.dropna(subset=['nombre'])
# Convertir les nombre en entiers
df['nombre'] = df['nombre'].astype(int)

# ──────────────────────────────────────────────────────────────────────────────────────

clean_path = os.path.join("data", "clean")

os.makedirs(clean_path, exist_ok=True)
df.to_csv(os.path.join(clean_path, "data.csv"), index=False)








