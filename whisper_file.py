#import whisper # remote or local transcription options
import openai
import os

openai.api_key = "Key-API" # replace "Key-API" with your api key 

def translate_in_chat():
    #model = whisper.load_model("medium") # Call the model whisper
    #result = model.transcribe("vocal0.wav") # audio transcription
    audio_file = open("vocal0.wav", "rb") # open audio
    transcript = openai.Audio.transcribe("whisper-1", audio_file) # audio transcription
    return transcript["text"]
# end translate_in_chat