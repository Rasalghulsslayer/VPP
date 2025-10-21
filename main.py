"""
Ce script permet de run complétement notre pipeline ETL avec les étapes suivantes :
1. Extraire les données utilisateurs du fichier CSV
2. Nettoyer et transformer les données
3. Charger les données dans la database PostgreSQL 

A run avec: python main.py
"""

### Modifications à faire selon votre environnement

"""
Dans generate_data.py, modifier la ligne 90 pour enregistrer le CSV dans le bon dossier de votre environnement 
"""

from data.generate_data import generate_data
from etl.clean_survey_data import clean
from etl.load_data import load_to_database, test_database_connection

def main():
    print("🚀 Démarrage du pipeline ETL...")
    print("=" * 50)

    # Etape 1 : Générer les données
    print("\n=== GENERATION ===")
    generate_data()

    print("✅ Génération des données terminée. Voir les fichiers users_profiles et users_travels")

    # Etape 2 : Nettoyer les données
    print("\n=== NETTOYAGE ===")
    clean()

    print("✅ Nettoyage des données terminée. Voir les fichiers data_profiles_clean et data_travels_clean")

    # Etape 3 : Charger les données dans la base de données
    print("\n=== CHARGEMENT ===")
    load_to_database("data/data_profiles_clean.csv", table_name="users_profiles")
    load_to_database("data/data_travels_clean.csv", table_name="users_travels")

    print("✅ Chargement des données terminé.")

    # Etape 4 : Vérifier le chargement
    print("\n=== VERIFICATION ===")
    test_database_connection()

    print("\n🎉 ETL Pipeline completed!")
    print("=" * 50)

main()