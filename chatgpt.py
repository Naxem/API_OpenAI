import openai 
openai.api_key = ""
messages = []

def start_assisant():
    messages.append({"role": "system", "content": "Your are a Doctorate in IT. You answer concisely and mischievously as possible for each response. If you are generating a list, do not have too many items. All numbers have to be spelled out."})

def create_message(msg):
    messages.append({"role": "user", "content": msg})

def chatgptF():
    completion = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = messages
    )

    response_chatgpt = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response_chatgpt})
    print(response_chatgpt)
