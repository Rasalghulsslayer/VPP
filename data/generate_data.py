import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

def generate_interests(interests):
    chosen_main = random.sample(list(interests.keys()), random.randint(1, 3))
    chosen_sub = []
    for main in chosen_main:
        sub = random.choice(interests[main])
        chosen_sub.append(f"{main}:{sub}")
    return "|".join(chosen_main), "|".join(chosen_sub)

def generate_data():
    """
    Génère des données utilisateur fictives pour les utilisateurs
    et les sauvegarde dans des fichiers CSV.
    """
    fake = Faker("fr_FR")
    random.seed(42)

    # Paramètres
    n_users = 1000

    # Options
    travel_reasons = ['Travail/études', 'Autre', 'Visite famille/amis', 'Loisirs/vacances']
    expectations = ['Discussion sympa', 'Rester tranquille', 'Réseautage pro', 'Échanger sur un sujet commun', 'Autre']
    conversation_triggers = ['Ça dépend', 'Jamais', 'Le trajet est long', 'La conversation est légère', 'Il/elle partage mes centres d\'intérêt']
    personalities = ['Drôle', 'Sérieux(se)', 'Calme', 'Autre', 'Introverti(e)', 'Peu importe', 'Extraverti(e)']
    topics = ['Politique', 'Religion', 'Sexe', 'Argent', 'Santé', 'Autre']
    languages = ['Français', 'Anglais', 'Espagnol', 'Italien', 'Allemand', 'Autre']
    genders = ['Non-binaire', 'Préfère ne pas dire', 'Homme', 'Femme']
    orientations = ['Hétérosexuel(le)', 'Homosexuel(le)', 'Bisexuel(le)', 'Pansexuel(le)', 'Asexuel(le)', 'Autre', 'Préfère ne pas dire']

    # Centres d'intérêts
    interests = {
        "Lecture": ["Romans", "Essais", "Développement personnel", "BD/Mangas"],
        "Musique": ["Pop", "Rock", "Rap/Hip-hop", "Électro", "Jazz/Blues", "Classique", "World"],
        "Technologie": ["Programmation", "IA", "Gadgets", "Cybersécurité", "Innovation"],
        "Entrepreneuriat": ["Création", "Investissement", "Marketing", "Design produit"],
        "Sport": ["Football", "Basket", "Rugby", "Running", "Cyclisme", "Yoga", "Randonnée", "Escalade", "Ski"],
        "Cuisine": ["Gastronomie FR", "Cuisine du monde", "Végétarien/vegan", "Pâtisserie"],
        "Voyage": ["Road trip", "City trip", "Nature", "Culture & musées"],
        "Jeux vidéo": ["Action", "FPS", "RPG", "Casual", "Retro"],
        "Photographie": ["Portrait", "Paysage", "Urbain", "Édition"],
        "Arts & culture": ["Cinéma", "Théâtre", "Arts visuels", "Histoire"],
        "Sciences": ["Biologie", "Physique", "Santé", "Sciences sociales"],
        "Podcasts": ["Actualité", "True crime", "Développement perso", "Tech", "Culture"]
    }


# Taux d’erreurs simulées
error_rate = 0.05

    # Containers
    profiles = []
    travels = []

    for _ in range(n_users):
        user_id = str(uuid.uuid4())
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(16, 70)
        gender = random.choice(genders)
        orientation = random.choice(orientations)
        languages_spoken = "|".join(random.sample(languages, random.randint(1, 3)))
        interests_main, interests_sub = generate_interests(interests)
        topics_to_avoid = "|".join(random.sample(topics, random.randint(1, 2)))
        preferred_personality = random.choice(personalities)
        self_personality = random.choice(personalities)
        created_at = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()

    # erreurs aléatoires sur profil
        if random.random() < error_rate:
            if random.random() < 0.3:
                interests_sub = str(random.randint(1, 9999))
            if random.random() < 0.2:
                age = random.choice(["unknown", "na", "N/A"])

        profiles.append([
            user_id, first_name, last_name, age, gender, orientation, languages_spoken,
            interests_main, interests_sub, topics_to_avoid, preferred_personality, self_personality, created_at
        ])

        # Infos voyage (dépendantes du trajet)
        travel_reason = random.choice(travel_reasons)
        expectation = random.choice(expectations)
        conv_trigger = random.choice(conversation_triggers)
        openness_score = random.randint(1, 5)

        travels.append([
            user_id, travel_reason, expectation, conv_trigger, openness_score
        ])

    # Colonnes
    profile_cols = [
        "user_id", "first_name", "last_name", "age", "gender", "sexual_orientation",
        "languages_spoken", "interests_main", "interests_sub", "topics_to_avoid",
        "preferred_personality", "self_personality", "created_at"
    ]

    travel_cols = [
        "user_id", "travel_reason", "expectations_from_neighbor",
        "conversation_trigger", "openness_score"
    ]

    # DataFrames
    df_profiles = pd.DataFrame(profiles, columns=profile_cols)
    df_travels = pd.DataFrame(travels, columns=travel_cols)

    # Sauvegarde CSV
    df_profiles.to_csv("data/users_profiles.csv", index=False)
    df_travels.to_csv("data/users_travels.csv", index=False)

    print("✅ CSV générés avec succès :")
    print("- users_profiles.csv :", df_profiles.shape)
    print("- users_travels.csv  :", df_travels.shape)
    print(df_profiles.head())
    print(df_travels.head())


generate_data()