import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Paramètres d'enregistrement
trigger_words = ["ok michel", "OK MICHEL", "Ok Michel", "ok Michel", "ok michelle", "OK MICHELLLE", "Ok Michellle", "ok Michellle"]  # Mot déclencheur à détecter
duration = 10  # Durée maximale d'enregistrement en secondes
boucle = True

# Configuration du recognizer
r = sr.Recognizer()

def enregistrement():
    global boucle
    freq = 44100
    # Enregistrement audio
    while boucle:
        with sr.Microphone() as source:
            print("En attente du mot déclencheur...")
            audio = r.listen(source)

            try:
                # Reconnaissance vocale
                text = r.recognize_google(audio, language="fr-FR")
                
                # Vérification des mots déclencheurs
                for trigger_word in trigger_words:
                    if trigger_word in text:
                        print(f"Mot déclencheur '{trigger_word}' détecté. Enregistrement audio démarré.")
                        #démarre l'enregistrement
                        audio = r.listen(source, timeout=duration)
                        print("Enregistrement audio terminé.")
                        
                        # Sauvegarde de l'audio dans un fichier WAV
                        with open("vocal0.wav", "wb") as f:
                            f.write(audio.get_wav_data())
                            boucle = False
                        break
                else:
                    print("Aucun mot déclencheur détecté.")
            except sr.UnknownValueError:
                print("Impossible de reconnaître la parole.")
            except sr.RequestError as e:
                print(f"Erreur lors de la requête au service de reconnaissance vocale : {e}")