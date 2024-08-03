import speech_recognition as sr
from pydub import AudioSegment
import os
import google.generativeai as genai
import os
from io import BytesIO

# Initialize the speech recognizer
recognizer = sr.Recognizer()
genai.configure(api_key="AIzaSyBvm81UbrcN3z7KFjlWxvbWGrD9r4K7dAU")

def call_ai_api(input_text):
    # Set up the model
    prompt = f"""
        Transforme le texte ci-dessous, qui est une transcription d'un enregistrement audio où un recruteur décrit un projet, en une description d'offre d'emploi complète et structurée. La description doit suivre le format ci-dessous :

        1. Description de l'activité de l'entreprise :
        2. Description du contexte du projet :
        3. Objectifs et livrables identifiés :
        4. Compétences fonctionnelles et techniques :

        Texte :
        "{input_text}"

        La description d'offre d'emploi doit être détaillée et couvrir les points suivants :
        - L'activité de l'entreprise et ses domaines d'expertise.
        - Le contexte du projet et sa pertinence pour l'entreprise.
        - Les objectifs spécifiques du projet et les livrables attendus.
        - Les compétences techniques et fonctionnelles requises pour le poste, ainsi que les conditions de travail (par exemple, la possibilité de travail en remote et la rémunération)."""

    # model = Cohere(cohere_api_key='pkIGBX2w2ybx28QS3UDdFKRauQFt2zQztUp0I8ZY')
    # response = model.invoke(prompt)
    # return  response
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "max_output_tokens": 5000000,
    }
    model = genai.GenerativeModel(model_name="gemini-1.0-pro-latest",
                                generation_config=generation_config)
    response = model.generate_content(prompt)
    return response.text


def audio_to_text(audio_data):
    with sr.AudioFile(BytesIO(audio_data)) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio,language='fr-FR')
            return text
        except sr.UnknownValueError:
            return "Unable to understand the audio"
        except sr.RequestError as e:
            return f"Service error: {e}"