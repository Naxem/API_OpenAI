import openai
import apiKey

openai.api_key = apiKey.key

def dallE(txt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=txt,
        size="1024x1024",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)