import enreAudio
import chatgpt
import whisper_file

def mainF():
    chatgpt.start_assisant()
    print("start enregistrement 5s")
    enreAudio.enregistrement(44100, 5)
    question = whisper_file.translate_in_chat()
    print(question)
    chatgpt.create_message(question)
    chatgpt.chatgptF()

mainF()