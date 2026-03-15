from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):

    score = analyzer.polarity_scores(text)

    compound = score['compound']

    # Emotion detection
    if compound >= 0.6:
        emotion = "excited"
    elif compound >= 0.2:
        emotion = "happy"
    elif compound <= -0.6:
        emotion = "angry"
    elif compound <= -0.2:
        emotion = "sad"
    else:
        emotion = "neutral"

    return emotion, compound