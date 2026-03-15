from emotion_detector import detect_emotion
from tts_engine import speak_text

text = input("Enter text: ")

emotion, intensity = detect_emotion(text)

print("Detected Emotion:", emotion)

speak_text(text, emotion, intensity)

print("Audio generated: output.wav")