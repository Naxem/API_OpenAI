import openai
import apiKey

openai.api_key = apiKey.key #replace "Key-API" with your api key in file (apiKey)

def dallE(txt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=txt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)
#end dallE