import openai
from config.key import key_openai

openai.api_key = key_openai
messages = []

#configurer ChatGPT avec un message système
def start_assisant(type):
    if type == 1: #pour vocal
        messages.append({"role": "system", "content": "Vous répondez de manière aussi concise que possible pour chaque réponse sans oublier des informations nécessaire ou intéressante . Si vous établissez une liste, ne prévoyez pas trop d'éléments."})
    elif type == 2: #écrit
        messages.append({"role": "system", "content": "Vous répondez à chaque question le plus précisément possible. Si nécessaire, faites une liste."})
    else:
        return print("Ereur type in start_assisant")
    return print("Success: phase 1")

#préparation question/message
def create_message(msg):
    messages.append({"role": "user", "content": msg})
    print("Success: phase 2")

#configure ChatGPT & récupére la reponse
def chatgptF():
    completion = openai.ChatCompletion.create(
        model= "gpt-4-turbo-2024-04-09",
        messages = messages
    )

    response_chatgpt = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response_chatgpt})
    print("Success: phase 3")
    return response_chatgpt