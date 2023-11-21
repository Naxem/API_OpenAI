import openai
import apiKey

openai.api_key = apiKey.key #replace "Key-API" with your api key in file (apiKey)
messages = []

#configure ChatGPT with a system message, you can modify this phrase to personalize your assistant's responses. 
def start_assisant(type):
    if type == 1:
        messages.append({"role": "system", "content": "You answer concisely as possible for each response. If you are generating a list, do not have too many items."})
    elif type == 2:
        messages.append({"role": "system", "content": "You answer each question as precisely as possible. If necessary, make a list."})
    elif type == 3:
        messages.append({"role": "system", "content": "You're going to have to help me by replying with the prompt to generate the image with Dall-E, you're going to have to generate the prompt with what I give you and improve so that Dall-E gives a perfect image."})
    else:
        print("Ereur type in start_assisant")
#end start_assisant

#send question/message
def create_message(msg):
    messages.append({"role": "user", "content": msg})
#end create_message

#configure ChatGPT here to use version 3.5 turbo
def chatgptF():
    completion = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = messages
    )

    response_chatgpt = completion.choices[0].message.content #retrieves the answer
    messages.append({"role": "assistant", "content": response_chatgpt})
    return response_chatgpt
#end chatgptF