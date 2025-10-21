# VPP
Bienvenue chers intrépides, préparez vous pour le voyage de votre vie en faisant confiance à "Un Voyage Presque Parfait" !

## Présentation du Projet 

Ce projet est un simple processus d'intégration automatisé ETL (Extraction, Transformation et Chargement) implémenté en Python. 
Notre pipeline a pour but de : 

- Extraire les données issues d'un fichier csv d'utilisateurs de notre application (fichier issu de réponse à un formulaire)
- Transformer ces données en les nettoyant,
- Chager les données finales dans la base de données de notre application

## Structure du projet

````
VPP/
│
├── data/                           
│   ├── generate_data.py            # Fonction générant 1000 profils utilisateurs
|   ├── users_profiles.csv          # Fichier contenant les informations utilisateurs (généré par generate_data.py)
|   └── users_travels.csv           # Fichier contenant les informations utilisateurs relatives au voyage concerné
│
├── etl/
│   ├── clean_survey_data.py        # Code pour le nettoyage des données
│   └── load_data.py                # Code pour le chargement des données dans la database
│
├── README.md                       # Documentation du projet
├── requirements.txt                # Liste des dépendances Python à avoir 
└── main.py                         # A lancer pour lancer la création de la pipeline
````

## Prérequis 

Pour run notre pipeine, les versions suivantes sont nécessaires dans votre système : 

- **Python 3.X**
- **pip** (programme d'installation du paquet python)
- **PostgreSQL 12** ou version plus récente


## Setup 

1. **Fork** le repository sur votre Github account
2. **Clone** votre fork localement avec :

```bash
git clone https://github.com/YOUR_USERNAME/VPP.git
cd VPP
```
3. Installez les dépendances de Python nécessaires :
   
 ```bash
 pip install -r requirements.txt
 ```
4. Créez la **PostgreSQL database** :

```bash
# Vérifier qu'on a bien les dépendances
python3 -m pip install psycopg2-binary sqlalchemy pandas

# Se connecter :
sudo -u postgres psql
   
# Dans PSQLn créer la database
CREATE DATABASE vpp_users_db;
   
# Quitter et se reconnecter à la nouvelle database
\q
psql -U your_username -d vpp_users_db

# Créer des tables
\i database_setup.sql
```

## Configuration de la connexion à la database

Modifiez la database dans `src/load_data.py` :

```python
DATABASE_CONFIG = {
    'username': 'your_username',      # Replace with your PostgreSQL username
    'password': 'your_password',      # Replace with your PostgreSQL password
    'host': 'localhost',
    'port': '5432',
    'database': 'airlife_db'
}
```

