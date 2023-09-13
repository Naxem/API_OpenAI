import enreAudio
import chatgpt
import whisper_file

def mainF():
    chatgpt.start_assisant()
    enreAudio.enregistrement()
    question = whisper_file.translate_in_chat()
    print(question)
    chatgpt.create_message(question)
    chatgpt.chatgptF()
    enreAudio.boucle = True
mainF()