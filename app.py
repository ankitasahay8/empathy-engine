from flask import Flask, request
from emotion_detector import detect_emotion
from tts_engine import speak_text

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        text = request.form["text"]

        emotion, intensity = detect_emotion(text)

        speak_text(text, emotion, intensity)

        return f"""
        <h2>Emotion Detected: {emotion}</h2>
        <p>Audio Generated Successfully</p>

        <audio controls>
            <source src="/static/output.wav" type="audio/wav">
        </audio>

        <br><br>

        <a href="/">Try Another Text</a>
        """

    return """
    <h1>Empathy Engine</h1>

    <form method="post">
        <input name="text" style="width:300px;height:40px">
        <br><br>
        <button type="submit">Generate Voice</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)