# 🌍 Planificateur de Voyage IA ✈️

Le **Planificateur de Voyage IA** est une application interactive développée avec Streamlit et alimentée par l'API Mistral. Elle aide les utilisateurs à planifier leurs voyages en générant des conseils personnalisés en fonction de leurs préférences et de leur budget.

## 🚀 Fonctionnalités

- **Planification de voyage interactive** : Répondez à une série de questions pour affiner votre voyage idéal.
- **Recommandations personnalisées** : L'IA génère un programme de voyage sur mesure en fonction de votre destination, budget, durée du séjour et préférences d'activités.
- **Conseils pratiques** : L'application fournit des informations essentielles sur les visas, la santé et d'autres aspects liés au voyage.
- **Génération de PDF** : Obtenez un itinéraire détaillé sous format PDF, incluant des recommandations et des options de prix et confort.

## 🛠️ Installation
Avant de commencer, assurez-vous d'avoir installé Python et `pip`.

1. Clonez ce projet :
   ```sh
   git clone https://github.com/votre-repo/chatbot-voyage.git
   cd chatbot-voyage
   ```
2. Installez les dépendances nécessaires :
   ```sh
   pip install -r requirements.txt
   ```
3. Créez un fichier `.env` à la racine du projet et ajoutez votre clé API Mistral :
   ```
   MISTRAL_API_KEY=votre_cle_api_ici
   ```
4. Lancez l'application Streamlit :
   ```sh
   streamlit run chatbot.py
   ```

## 🛠️ Technologies utilisées
- [Streamlit](https://streamlit.io/) : Interface utilisateur interactive.
- [Mistral AI](https://mistral.ai/) : Génération de recommandations basées sur l'IA.
- [FPDF](https://pyfpdf.readthedocs.io/en/latest/) : Génération de fichiers PDF.
- [Python-dotenv](https://pypi.org/project/python-dotenv/) : Gestion des variables d'environnement.
- [Requests](https://docs.python-requests.org/en/latest/) : Envoi des requêtes HTTP vers l'API Mistral.

## ⚙️ Prérequis
Avant d'exécuter l'application, assurez-vous d'avoir installé :
- Python 3.8+
- Les bibliothèques Python suivantes :
  ```sh
  pip install streamlit requests python-dotenv fpdf
  ```

## 📄 Licence
Ce projet est sous licence [MIT](LICENSE). Vous êtes libre de l'utiliser, le modifier et le partager.

## 📝 Auteur
Projet développé par Melvin 3374. 

Pour toute question, n'hésitez pas à me contacter ! 😊
