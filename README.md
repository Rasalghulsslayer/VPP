# VPP
Bienvenue chers intrépides, préparez vous pour le voyage de votre vie en faisant confiance à "Un Voyage Presque Parfait" !

## Présentation du Projet 

Ce projet est un simple processus d'intégration automatisé ETL (Extraction, Transformation et Chargement) implémenté en Python. 
Notre pipeline a pour but de : 

- Extraire les données issues d'un fichier csv d'utilisateurs de notre application (fichier issu de réponse à un formulaire)
- Transformer ces données en les nettoyant,
- Chager les données finales dans la base de données de notre application

## Structure du projet

VPP/
│
├── data/                           
│   ├── data_survey.csv             # Données utilisateurs issus du questionnaire
|   └── data_survey_clean.csv       # Données à la fin du processus de traitement (nettoyage)
│
├── etl/
│   ├── clean_survey_data.py        # Code pour le nettoyage des données
│   └── load.py                     # Code pour le chargement des données A FAIRE
│
├── README.md                       # Documentation du projet
├── requirements.txt                # Liste des dépendances Python à avoir 
└── main.py                         # A FAIRE

## Prérequis 

Pour run notre pipeine, les versions suivantes sont nécessaires dans votre système : 

- **Python 3.X**
- **pip** (programme d'installation du paquet python)


