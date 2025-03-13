import openai
import os
from dotenv import load_dotenv

# Charger la clé API depuis le fichier .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Vérifier que la clé API est bien chargée
if not API_KEY:
    raise ValueError("⚠️ Clé API OpenAI non trouvée. Vérifie ton fichier .env !")

# Créer le client OpenAI
client = openai.OpenAI(api_key=API_KEY, base_url="https://api.openai.com/v1")

def generer_reponse(messages):
    """Génère une réponse avec GPT-3.5."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Erreur : {str(e)}"

def obtenir_infos_visa(destination):
    """Obtient les informations sur les visas pour une destination donnée."""
    messages = [{"role": "system", "content": "Tu es un assistant utile."},
                {"role": "user", "content": f"Quels sont les requis de visa pour {destination} ?"}]
    return generer_reponse(messages)

def obtenir_conseils_sante(destination):
    """Obtient les conseils de santé pour une destination donnée."""
    messages = [{"role": "system", "content": "Tu es un assistant utile."},
                {"role": "user", "content": f"Quels sont les conseils de santé pour {destination} ?"}]
    return generer_reponse(messages)