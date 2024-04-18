import speech_recognition as sr

#Recording parameters
trigger_words = ["ok michel", "OK MICHEL", "Ok Michel", "ok Michel", "ok michelle", "OK MICHELLLE", "Ok Michellle", "ok Michellle"]  #Trigger word
duration = 10  #Maximum recording time in seconds
boucle = True

#Recognizer configuration
r = sr.Recognizer()

def enregistrement():
    global boucle
    #freq = 44100
    #Audio recording
    while boucle:
        with sr.Microphone() as source:
            print("Waiting for the trigger word...")
            audio = r.listen(source)

            try:
                #Voice recognition
                text = r.recognize_google(audio, language="fr-FR")
                
                #Checking trigger words
                for trigger_word in trigger_words:
                    if trigger_word in text:
                        print(f"Trigger word '{trigger_word}' detected. Audio recording started.")
                        #Starts recording
                        audio = r.listen(source, timeout=duration)
                        print("Audio recording complete.")
                        
                        #Saving audio as a WAV file
                        with open("vocal0.wav", "wb") as f:
                            f.write(audio.get_wav_data())
                            boucle = False
                        break
                else:
                    print("No trigger word detected.")
            except sr.UnknownValueError:
                print("Impossible to recognize speech.")
            except sr.RequestError as e:
                print(f"Error when requesting speech recognition service : {e}")