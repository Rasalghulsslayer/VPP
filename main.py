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

from data.generate_data import generate_interests

def main():
    print("🚀 Démarrage du pipeline ETL...")
    print("=" * 50)

    # Etape 1 : Générer les données
    print("\n=== GENERATION ===")
    generate_data()

    print("✅ Génération des données terminée. Voir les fichiers users_profiles et users_travels")

    # Etape 2 : Nettoyer les données
    print("\n=== NETTOYAGE ===")