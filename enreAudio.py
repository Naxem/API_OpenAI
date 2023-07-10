import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import wave

def enregistrement(freq, duration):
    #démarre l'enregistrement
    recording = sd.rec(int(duration * freq),
        samplerate=freq, channels=2)
    sd.wait()

    transform_to_wav(recording, freq, duration)


def transform_to_wav(recording, freq, duration):
    #wavio pour convertir le NumPy en fichier audio
    wv.write("vocal0.wav", recording, freq, sampwidth=2)

    filename = "vocal0.wav"

    #test le fichier audio
    try:
        with wave.open(filename, 'rb') as audio_file:
            frames = audio_file.getnframes()
            channels = audio_file.getnchannels()
            sample_width = audio_file.getsampwidth()
            framerate = audio_file.getframerate()

            # Vérifier si les propriétés sont valides pour la lecture
            if frames > 0 and channels > 0 and sample_width > 0 and framerate > 0:
                print("Le fichier audio est valide et peut être lu.")
            else:
                print("Le fichier audio est invalide.")
    except wave.Error:
        print("Impossible d'ouvrir le fichier audio.")