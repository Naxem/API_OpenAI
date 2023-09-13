import whisper

def translate_in_chat():
    model = whisper.load_model("medium") #Call the model whisper
    result = model.transcribe("vocal0.wav") #audio transcription
    return result["text"]
# end translate_in_chat