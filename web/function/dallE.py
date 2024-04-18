import openai
from config.key import key_openai

openai.api_key = key_openai

#Configure dall-e & récupére le résultat de l'image
def dallE(txt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=txt,
        size="1024x1024",
        n=1, #nombre d'image
    )

    image_url = response.data[0].url
    return image_url