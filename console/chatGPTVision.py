import apiKey
import base64
import fileinput
import requests

api_key = apiKey.key
messages = []

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

#configure ChatGPT here to use version 4 vision
def chatgptVision(img, txt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{txt}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img}"}
                    }
                ]
            }
        ],
        "max_tokens": 1500
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

def startVision(txt):
   print("Entrez le chemin de l'image :")
   for line in fileinput.input():
        image_path = line.strip()
        
        # Traitement de l'image
        img64 = encode_image(image_path)
        print(chatgptVision(img64, txt))