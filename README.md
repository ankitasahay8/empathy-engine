# Empathy Engine – Giving AI a Human Voice

## Overview

The Empathy Engine is a Python-based AI system that converts text into expressive speech by dynamically adjusting voice characteristics based on the detected emotion in the text.

The system analyzes the sentiment of the input using VADER sentiment analysis and maps emotions to different speech modulation settings using SSML (Speech Synthesis Markup Language). This allows the generated speech to sound more natural and emotionally expressive.

The project also includes a simple web interface where users can enter text and instantly hear the generated audio.

---

## Features

* Text input from user
* Emotion detection using VADER sentiment analysis
* Emotion-to-voice mapping
* Voice modulation using SSML
* Audio generation using Google Cloud Text-to-Speech
* Web interface using Flask
* Embedded audio player for playback

---

## Supported Emotions

The system currently detects multiple emotional states:

* Excited
* Happy
* Sad
* Angry
* Neutral

Each emotion adjusts speech characteristics such as **pitch**, **rate**, and **emphasis**.

---

## Technologies Used

* Python
* Flask (Web Interface)
* VADER Sentiment Analysis
* Google Cloud Text-to-Speech
* SSML (Speech Synthesis Markup Language)

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/empathy-engine.git
cd empathy-engine
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Configure Google Cloud Credentials

1. Create a Google Cloud project
2. Enable the **Text-to-Speech API**
3. Create a **Service Account**
4. Download the JSON credentials file
5. Set the environment variable:

Windows:

```
setx GOOGLE_APPLICATION_CREDENTIALS "your_credentials.json"
```

Place the credentials file inside the project folder.

---

## Run the Application

Start the web application:

```
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

Enter text and the system will generate expressive speech based on detected emotion.

---

## Emotion to Voice Mapping Logic

| Emotion | Pitch           | Rate   | Effect                  |
| ------- | --------------- | ------ | ----------------------- |
| Excited | Higher          | Fast   | Energetic speech        |
| Happy   | Slightly Higher | Medium | Positive tone           |
| Sad     | Lower           | Slow   | Calm and subdued speech |
| Angry   | Emphasized      | Fast   | Strong emphasis         |
| Neutral | Normal          | Normal | Default speech          |

SSML tags such as `<prosody>`, `<emphasis>`, and `<break>` are used to control speech modulation.

---

## Project Structure

```
empathy-engine
│
├ app.py
├ main.py
├ emotion_detector.py
├ ssml_tts.py
├ tts_engine.py
├ requirements.txt
├ README.md
│
└ static
     └ output.mp3
```

---

## Example

Input:

```
I am extremely excited about this project!
```

Detected Emotion:

```
Excited
```

Output:

Speech generated with higher pitch and faster rate.

---

## Future Improvements

* More granular emotion detection
* Emotion intensity scaling
* Improved UI design
* Support for additional voices and languages
