import pandas as pd
import numpy as np
import os
import re


# Charger le CSV
df = pd.read_csv("data/data_survey.csv")
print(f"Dataset original: {df.shape[0]} lignes, {df.shape[1]} colonnes")

# ==================== NETTOYAGE PAR COLONNE ====================

def clean_data(df):
    """
    Nettoie toutes les colonnes du dataset pour préparer l'entraînement ML
    """
    df_clean = df.copy()
    
    # 1. USER_ID - Vérifier le format UUID (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
    uuid_pattern = re.compile(r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$')
    def is_valid_uuid(uid):
        return bool(uuid_pattern.match(str(uid)))
    
    invalid_user_ids = ~df_clean['user_id'].apply(is_valid_uuid)
    if invalid_user_ids.any():
        for idx in df_clean[invalid_user_ids].index:
            fname = df_clean.at[idx, 'first_name']
            lname = df_clean.at[idx, 'last_name']
            print(f"{fname} {lname} veuillez vous reconnecter")
        df_clean = df_clean[~invalid_user_ids].reset_index(drop=True)
    
    # 2. FIRST_NAME and LAST_NAME - Standardize case and check that they are strings without digits
    def clean_name(name):
        if pd.isna(name):
            return name
        name = str(name).strip().title()
        # If the name contains a digit, replace with NaN
        if re.search(r'\d', name):
            return np.nan
        return name

    df_clean['first_name'] = df_clean['first_name'].apply(clean_name)
    df_clean['last_name'] = df_clean['last_name'].apply(clean_name)
    
    # 3. TRAVEL_REASON - Nettoyer les codes incorrects
    valid_travel_reasons = ['Travail/études', 'Autre', 'Visite famille/amis', 'Loisirs/vacances']
    # Remplacer les codes TRV_* par NaN
    df_clean['travel_reason'] = df_clean['travel_reason'].apply(
        lambda x: x if x in valid_travel_reasons else np.nan
    )

    # 4. EXPECTATIONS_FROM_NEIGHBOR - Nettoyer les valeurs incorrectes
    valid_expectations = ['Discussion sympa', 'Rester tranquille', 'Réseautage pro', 'Échanger sur un sujet commun', 'Autre']
    df_clean['expectations_from_neighbor'] = df_clean['expectations_from_neighbor'].apply(
        lambda x: x if x in valid_expectations else np.nan
    )

    # 5. INTERESTS_MAIN - Nettoyer les valeurs incorrectes
    valid_main_interests = [
        'Sport', 'Entrepreneuriat', 'Sciences', 'Arts & culture', 'Musique', 'Voyage', 'Podcasts',
        'Cuisine', 'Technologie', 'Photographie', 'Lecture', 'Jeux vidéo'
    ]
    df_clean['interests_main'] = df_clean['interests_main'].apply(
        lambda x: x if x in valid_main_interests else np.nan
    )

    # 6. INTERESTS_SUB - Nettoyer les valeurs incorrectes
    valid_sub_interests = [
        'Football', 'Basketball', 'Tennis', 'Natation', 'Running', 'Cyclisme', 'Startup', 'Innovation', 'Biologie', 'Physique',
        'Chimie', 'Peinture', 'Théâtre', 'Cinéma', 'Rock', 'Jazz', 'Classique', 'Pop', 'Rap',
        'Road trip', 'Randonnée', 'Cuisine du monde', 'Pâtisserie', 'Développement web', 'IA',
        'Data science', 'Portrait', 'Paysage', 'Roman', 'BD', 'Manga', 'FPS', 'RPG', 'Stratégie'
    ]
    df_clean['interests_sub'] = df_clean['interests_sub'].apply(
        lambda x: x if x in valid_sub_interests else np.nan
    )

    # 7. CONVERSATION_TRIGGER - Nettoyer les valeurs incorrectes
    valid_triggers = ['Ça dépend', 'Jamais', 'Le trajet est long', 'La conversation est légère', 'Il/elle partage mes centres d\'intérêt']
    df_clean['conversation_trigger'] = df_clean['conversation_trigger'].apply(
        lambda x: x if x in valid_triggers else np.nan
    )

    # 8. PREFERRED_PERSONALITY - Nettoyer les valeurs incorrectes
    valid_personalities = ['Drôle', 'Sérieux(se)', 'Calme', 'Autre', 'Introverti(e)', 'Peu importe', 'Extraverti(e)']
    df_clean['preferred_personality'] = df_clean['preferred_personality'].apply(
        lambda x: x if x in valid_personalities else np.nan
    )

    # 9. SELF_PERSONALITY - Utiliser les mêmes valeurs valides pour nettoyer les valeurs incorrectes
    df_clean['self_personality'] = df_clean['self_personality'].apply(
        lambda x: x if x in valid_personalities else np.nan
    )

    # 10. TOPICS_TO_AVOID - Standardiser le format
    valid_topics = ['Politique', 'Religion', 'Sexe', 'Argent', 'Santé', 'Autre']
    df_clean['topics_to_avoid'] = df_clean['topics_to_avoid'].apply(
        lambda x: x if x in valid_topics else np.nan
    )

    # 12. LANGUAGES_SPOKEN - Nettoyer les valeurs incorrectes
    valid_languages = ['Français', 'Anglais', 'Espagnol', 'Italien', 'Allemand', 'Autre']
    df_clean['languages_spoken'] = df_clean['languages_spoken'].apply(
        lambda x: x if x in valid_languages else np.nan
    )

    # 13. OPENNESS_SCORE - Nettoyer les valeurs incorrectes
    # Les valeurs valides sont 0, 1, 2, 3, 4, 5, 6
    valid_scores = [0, 1, 2, 3, 4, 5, 6]
    df_clean['openness_score'] = df_clean['openness_score'].apply(
        lambda x: x if x in valid_scores else np.nan
    )

    # 11. AGE - Convertir en numérique et nettoyer
    # Convertir les âges en numérique
    df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
    # Remplacer les valeurs manquantes par NaN
    df_clean['age'] = df_clean['age'].apply(lambda x: x if x >= 16 and x <= 120 else np.nan)
    # S'assurer que les âges sont réalistes (16-120)
    df_clean['age'] = df_clean['age'].clip(16, 120)
  
    # 14. GENDER - Standardiser les valeurs
    valid_gender = {
        'Non-binar': 'Non-binaire',
        'Prefere pas': 'Préfère ne pas dire',
        'Hommee': 'Homme'
    }
    df_clean['gender'] = df_clean['gender'].apply(
        lambda x: x if x in valid_gender else np.nan
    )

    # 15. SEXUAL_ORIENTATION - Pas de nettoyage nécessaire
    valid_sexual_orientations = [
        'Hétérosexuel(le)', 'Homosexuel(le)', 'Bisexuel(le)', 'Pansexuel(le)', 'Asexuel(le)', 'Autre', 'Préfère ne pas dire'
    ]
    df_clean['sexual_orientation'] = df_clean['sexual_orientation'].apply(
        lambda x: x if x in valid_sexual_orientations else np.nan
    )
    
    return df_clean

# ==================== EXÉCUTION ====================

# Nettoyer les données
df_clean = clean_data(df)

print(f"Dataset nettoyé: {df_clean.shape[0]} lignes, {df_clean.shape[1]} colonnes")
df_clean.to_csv("data/data_survey_clean.csv", index=False)
print("Données nettoyées enregistrées dans data_survey_clean.csv")

