import openai
openai.api_key = "Key-API" # replace "Key-API" with your api key 
messages = []

# configure ChatGPT with a system message, you can modify this phrase to personalize your assistant's responses. 
def start_assisant():
    messages.append({"role": "system", "content": "You answer concisely as possible for each response. If you are generating a list, do not have too many items. All numbers have to be spelled out."})
# end start_assisant


# send question/message
def create_message(msg):
    messages.append({"role": "user", "content": msg})
# end create_message

# configure ChatGPT here to use version 3.5 turbo
def chatgptF():
    completion = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = messages
    )

    response_chatgpt = completion.choices[0].message.content # retrieves the answer
    messages.append({"role": "assistant", "content": response_chatgpt})
    print(response_chatgpt) # displays the answer
# end chatgptF