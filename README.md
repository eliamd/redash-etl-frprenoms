# 🇫🇷  Analyse des prénoms français (1900–2022)

🎯 **Projet personnel de Data Engineering** construit autour des données de prénoms publiées par l'INSEE.  
L'objectif : créer un **pipeline ETL complet**, avec **visualisation interactive** via Redash.

---

## 📌 Fonctionnalités

- 🔎 Extraction des données officielles depuis [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/fichier-des-prenoms/)
- 🧹 Transformation et nettoyage avec Python (`pandas`)
- 🗃️ Stockage dans **PostgreSQL**
- 📈 Visualisation des données avec **Redash**
- ⚙️ Docker Compose prêt à l'emploi
- 🔁 Makefile pour automatiser tout le pipeline

---

## 📸 Aperçu

![dashboard demo](https://i.imgur.com/puM4ITB.png)

## 🔧 Lancer le projet
1. **Cloner le dépôt :**
   ```bash
   git clone```
2. **Lancer le Makefile**
    ```bash
    make all
    ```
3. **Accéder à Redash :**
Ouvrir votre navigateur et aller à `http://localhost:5000`
