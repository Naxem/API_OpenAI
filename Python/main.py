import enreAudio
import chatgpt
import whisper_file
import dallE
import chatGPTVision

def mainF():
    print("Entré le choix que vous voulez")
    print("Choix 1 = assistant vocal, Choix 2 = chat gpt, choix 3 = Dall-E avec chatGPT et Choix 4 = Dall-E, choix 5 = Vision")
    choix1 = int(input("Choix entre 1 2 3 4 5 : "))
    #chaque choix va lancer un function diférente
    if choix1 == 1:
        chatgptVoc()
    elif choix1 == 2:
        chatgptText()
    elif choix1 == 3:
        DallEAndGPT()
    elif choix1 == 4:
        DallE()
    elif choix1 == 5:
        GPT4Vision()
    else:
        print("Erreur: choix pas dans la liste")
#end mainF

def chatgptVoc():
    chatgpt.start_assisant(1)
    enreAudio.enregistrement()
    question = whisper_file.translate_in_chat()
    print(question) #Question display
    chatgpt.create_message(question)
    chatgpt.chatgptF()
    enreAudio.boucle = True
#end chatgptVoc

def chatgptText():
    chatgpt.start_assisant(2)
    question = input("Entrez votre question pour Mr Gpt : ")
    print(question)
    chatgpt.create_message(question)
    reponse = chatgpt.chatgptF()
    print(reponse) #Display the answer
#end chatgptText

def DallEAndGPT():
    chatgpt.start_assisant(3)
    question = input("Entrez une description d'image pour que ChatGPT fasse le prompt : ")
    chatgpt.create_message(question)
    reponse = chatgpt.chatgptF()
    print(reponse) #Display the answer
    dallE.dallE(reponse)
#end DallEAndGPT

def DallE():
    text = input("Entrez une description pour l'image : ")
    dallE.dallE(text)
#end DallE

def GPT4Vision():
    text = input("Entrez une description pour Vision : ")
    chatGPTVision.startVision(text)
#end GPT4Vision
mainF()