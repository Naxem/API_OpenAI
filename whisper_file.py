import whisper

def translate_in_chat():
    model = whisper.load_model("medium")
    result = model.transcribe("vocal0.wav")
    print("Question : ", result["text"])
    return result["text"]