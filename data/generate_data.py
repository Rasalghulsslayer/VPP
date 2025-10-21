import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker("fr_FR")
random.seed(42)

# Paramètres
n_users = 1000

# Options
travel_reasons = ["Travail/études", "Loisirs/vacances", "Visite famille/amis", "Autre"]
expectations = ["Discussion sympa", "Rester tranquille", "Échanger sur un sujet commun", "Réseautage pro", "Autre"]
conversation_triggers = ["Il/elle partage mes centres d’intérêt", "La conversation est légère",
                         "Le trajet est long", "Jamais", "Ça dépend"]
personalities = ["Introverti(e)", "Extraverti(e)", "Sérieux(se)", "Drôle", "Calme", "Autre", "Peu importe"]
topics = ["Politique", "Religion", "Actualité sensible", "Vie privée", "Aucun"]
languages = ["Français", "Anglais", "Espagnol", "Allemand", "Italien", "Autre"]
genders = ["Femme", "Homme", "Non-binaire", "Préfère ne pas dire"]
orientations = ["Hétéro", "Homo", "Bi", "Pan", "Préfère ne pas dire"]

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

def generate_interests():
    chosen_main = random.sample(list(interests.keys()), random.randint(1, 3))
    chosen_sub = []
    for main in chosen_main:
        sub = random.choice(interests[main])
        chosen_sub.append(f"{main}:{sub}")
    return "|".join(chosen_main), "|".join(chosen_sub)

error_rate = 0.05
rows = []

for _ in range(n_users):
    user_id = str(uuid.uuid4())
    first_name = fake.first_name()
    last_name = fake.last_name()
    travel_reason = random.choice(travel_reasons)
    expectation = random.choice(expectations)
    interests_main, interests_sub = generate_interests()
    conv_trigger = random.choice(conversation_triggers)
    preferred_personality = random.choice(personalities)
    self_personality = random.choice(personalities)
    topics_to_avoid = "|".join(random.sample(topics, random.randint(1, 2)))
    languages_spoken = "|".join(random.sample(languages, random.randint(1, 3)))
    openness_score = random.randint(1, 5)
    age = random.randint(16, 70)
    gender = random.choice(genders)
    orientation = random.choice(orientations)
    created_at = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()

    # erreurs simulées
    if random.random() < error_rate:
        if random.random() < 0.3:
            interests_sub = str(random.randint(1, 9999))
        if random.random() < 0.2:
            age = random.choice(["unknown", "na", "N/A"])

    rows.append([
        user_id, first_name, last_name, travel_reason, expectation,
        interests_main, interests_sub, conv_trigger, preferred_personality, self_personality,
        topics_to_avoid, languages_spoken, openness_score, age, gender, orientation, created_at
    ])

columns = ["user_id", "first_name", "last_name", "travel_reason", "expectations_from_neighbor",
           "interests_main", "interests_sub", "conversation_trigger", "preferred_personality",
           "self_personality", "topics_to_avoid", "languages_spoken", "openness_score", "age",
           "gender", "sexual_orientation", "created_at"]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("/home/gmeffe/VPP/data/train_app_survey_1000.csv", index=False)
print(df.head())
