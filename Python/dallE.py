import openai
import apiKey

openai.api_key = apiKey.key #replace "Key-API" with your api key in file (apiKey)

def dallE(txt):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=txt,
        size="1024x1024",
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)
#end dallE