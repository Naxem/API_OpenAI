#import whisper # remote or local transcription options
import openai
#import os
import apiKey

openai.api_key = apiKey.key #replace "Key-API" with your api key in file (apiKey)

def translate_in_chat():
    #model = whisper.load_model("medium") # Call the model whisper
    #result = model.transcribe("vocal0.wav") # audio transcription
    audio_file = open("vocal0.wav", "rb") # open audio
    transcript = openai.Audio.transcribe("whisper-1", audio_file) # audio transcription
    return transcript["text"]
#end translate_in_chat