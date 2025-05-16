# 🌍 Planificateur de Voyage IA ✈️

Le **Planificateur de Voyage IA** est une application interactive développée avec Streamlit et alimentée par l'API Mistral. Elle aide les utilisateurs à planifier leurs voyages en générant des conseils personnalisés en fonction de leurs préférences et de leur budget.

## 🚀 Fonctionnalités

- **Planification de voyage interactive** : Répondez à une série de questions pour affiner votre voyage idéal.
- **Recommandations personnalisées** : L'IA génère un programme de voyage sur mesure en fonction de votre destination, budget, durée du séjour et préférences d'activités.
- **Conseils pratiques** : L'application fournit des informations essentielles sur les visas, la santé et d'autres aspects liés au voyage.
- **Génération de PDF** : Obtenez un itinéraire détaillé sous format PDF, incluant des recommandations et des options de prix et confort.

## 🛠️ Installation
Avant de commencer, assurez-vous d'avoir installé Docker, Docker Compose, Python 3.8+ et `pip`.

1. Clonez ce projet :
    ```sh
   git clone https://github.com/votre-repo/chatbot-voyage.git
   cd chatbot-voyage
   ```
3. Créez un environnement virtuel Python (optionnel mais recommandé) :
   ```sh
   python -m venv venv
   source venv/bin/activate   # Sur Windows : venv\Scripts\activate
   ```
4. Installez les dépendances nécessaires :
   ```sh
   pip install -r requirements.txt
   ```
5. Créez un fichier `.env` à la racine du projet et ajoutez votre clé API Mistral :
   ```
   MISTRAL_API_KEY=votre_cle_api_ici
   ```
6. Lancez les services Docker (PostgreSQL + API FastAPI) :
   
   ```sh
   docker-compose up --build
   ```
8. Lancez l’interface souhaitée :
  - Chatbot CLI (terminal) :
   ```sh
   docker exec -it voyage_api python app/chat_cli.py
   ```
- Chatbot GUI (interface web Streamlit) :
  ```sh
   streamlit run app/chatbot_gui.py
   ```

## 🛠️ Technologies utilisées
- [FastAPI](https://fastapi.tiangolo.com/) : Backend API REST pour gérer les requêtes.
- [PostgreSQL](https://www.postgresql.org/) : Base de données relationnelle déployée via Docker.
- [Docker & Docker Compose](https://www.docker.com/): Conteneurisation de l’application.
- [Streamlit](https://streamlit.io/) : Interface utilisateur interactive.
- [Mistral AI](https://mistral.ai/) : Génération de recommandations basées sur l'IA.
- [FPDF](https://pyfpdf.readthedocs.io/en/latest/) : Génération de fichiers PDF.
- [Python-dotenv](https://pypi.org/project/python-dotenv/) : Gestion des variables d'environnement.
- [Requests](https://docs.python-requests.org/en/latest/) : Envoi des requêtes HTTP vers l'API Mistral.
- [Typer (optionnel)](https://typer.tiangolo.com/) : Outil CLI Python pour le terminal.

## ⚙️ Prérequis
Avant d'exécuter l'application, assurez-vous d'avoir installé :
- Docker & Docker Compose installés (pour la base PostgreSQL et l’API).
- Python 3.8+ (pour les scripts CLI et GUI).

Les bibliothèques Python nécessaires (installées via requirements.txt ou manuellement) :
- Les bibliothèques Python suivantes :
  ```sh
  pip install fastapi uvicorn psycopg2-binary requests python-dotenv streamlit fpdf typer
  ```

## 📄 Licence
Ce projet est sous licence [MIT](LICENSE). Vous êtes libre de l'utiliser, le modifier et le partager.

## 📝 Auteur
Projet développé par Melvin 3374. 

Pour toute question, n'hésitez pas à me contacter ! 😊
