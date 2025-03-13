import streamlit as st
import requests
import os
from dotenv import load_dotenv
from fpdf import FPDF

# Charger les variables d'environnement
load_dotenv()

# Clé API Mistral
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Configuration de l'interface
st.set_page_config(page_title="Planificateur de Voyage IA", page_icon="✈️")
st.title("🌍 Planificateur de Voyage IA")
st.write("Discutez avec l'IA pour planifier votre voyage !")

# Initialiser l'état de session pour stocker la conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique de la conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Poser des questions supplémentaires pour affiner la demande
questions = [
    "🌎 Quelle est votre destination ?",
    "💰 Quel est votre budget approximatif pour ce voyage ?",
    "📅 Combien de jours prévoyez-vous de rester ?",
    "🎯 Quels types d'activités préférez-vous (culture, nature, gastronomie, etc.) ?",
    "🍽️ Avez-vous des restrictions alimentaires ou des préférences particulières ?"
]

# Si la conversation est vide, commencer par la première question
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "assistant", "content": questions[0]})
    with st.chat_message("assistant"):
        st.markdown(questions[0])

# Gérer les réponses de l'utilisateur
if prompt := st.chat_input("Votre réponse..."):
    # Ajouter la réponse de l'utilisateur à la conversation
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Vérifier si toutes les questions ont été posées
    if len(st.session_state.messages) < len(questions) * 2:  # *2 car chaque question et réponse compte
        # Poser la prochaine question
        next_question = questions[len(st.session_state.messages) // 2]
        st.session_state.messages.append({"role": "assistant", "content": next_question})
        with st.chat_message("assistant"):
            st.markdown(next_question)
    else:
        # Toutes les questions ont été posées, générer les conseils de voyage
        destination = st.session_state.messages[1]["content"]  # La réponse à la première question
        budget = st.session_state.messages[3]["content"]  # La réponse à la deuxième question
        duree = st.session_state.messages[5]["content"]  # La réponse à la troisième question
        activites = st.session_state.messages[7]["content"]  # La réponse à la quatrième question
        preferences_alimentaires = st.session_state.messages[9]["content"]  # La réponse à la cinquième question

        # Générer les conseils de voyage avec Mistral
        messages = [
            {"role": "system", "content": "Tu es un assistant utile pour planifier des voyages."},
            {"role": "user", "content": f"Je veux voyager à {destination}."},
            {"role": "user", "content": f"Mon budget est de {budget}."},
            {"role": "user", "content": f"Je reste {duree} jours."},
            {"role": "user", "content": f"J'aime {activites}."},
            {"role": "user", "content": f"Mes préférences alimentaires sont : {preferences_alimentaires}."}
        ]

        try:
            if MISTRAL_API_KEY:
                headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
                data = {"model": "mistral-tiny", "messages": messages}
                response = requests.post("https://api.mistral.ai/v1/chat/completions", json=data, headers=headers)
                conseils_voyage = response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            conseils_voyage = "Désolé, le service de chat est temporairement indisponible."

        # Afficher les conseils de voyage
        st.session_state.messages.append({"role": "assistant", "content": conseils_voyage})
        with st.chat_message("assistant"):
            st.markdown(conseils_voyage)

        # Ajouter des informations supplémentaires (visa, santé, etc.)
        infos_visa = "Pour un séjour de 30 jours à Bali, les ressortissants de nombreux pays (dont la France) bénéficient d'un visa gratuit à l'arrivée. Assurez-vous que votre passeport est valide pendant au moins 6 mois après la date d'entrée."
        conseils_sante = """
        - Vaccins recommandés : Hépatite A, Typhoïde, et Rage (si vous prévoyez des activités en plein air).
        - Évitez l'eau du robinet, préférez l'eau en bouteille.
        - Utilisez un répulsif anti-moustiques pour prévenir la dengue et le paludisme.
        """
        st.session_state.messages.append({"role": "assistant", "content": f"**Informations sur les visas :** {infos_visa}"})
        st.session_state.messages.append({"role": "assistant", "content": f"**Conseils de santé :** {conseils_sante}"})
        with st.chat_message("assistant"):
            st.markdown(f"**Informations sur les visas :** {infos_visa}")
            st.markdown(f"**Conseils de santé :** {conseils_sante}")

        # Bouton pour générer le PDF
        if st.button("Générer l'itinéraire PDF"):
            options = [
                {"description": "Option économique", "prix": "500"},
                {"description": "Option confort", "prix": "800"},
                {"description": "Option luxe", "prix": "1200"}
            ]
            generate_pdf(destination, conseils_voyage, options)

def generate_pdf(destination, content, options):
    """Génère un PDF avec l'itinéraire et les options de voyage."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Itinéraire pour {destination}", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=content)
    
    # Ajouter les options de prix et de confort
    pdf.ln(10)
    pdf.cell(200, 10, txt="Options de voyage :", ln=True, align="L")
    for option in options:
        pdf.multi_cell(0, 10, txt=f"{option['description']} - {option['prix']}€")
    
    pdf_output = f"itineraire_{destination}.pdf"
    pdf.output(pdf_output)

    st.download_button(
        label="Télécharger l'itinéraire",
        data=open(pdf_output, "rb").read(),
        file_name=pdf_output,
        mime="application/pdf"
    )