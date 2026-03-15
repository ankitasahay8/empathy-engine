import pyttsx3

engine = pyttsx3.init()

def speak_text(text, emotion, intensity):

    if emotion == "excited":
        engine.setProperty('rate', 220)

    elif emotion == "happy":
        engine.setProperty('rate', 190)

    elif emotion == "sad":
        engine.setProperty('rate', 130)

    elif emotion == "angry":
        engine.setProperty('rate', 170)

    else:
        engine.setProperty('rate', 150)

    engine.setProperty('volume', min(1.0, abs(intensity) + 0.5))

    engine.save_to_file(text, "static/output.wav")
    engine.runAndWait()