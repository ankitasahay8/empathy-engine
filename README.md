# Empathy Engine – Giving AI a Human Voice

## Overview

The Empathy Engine is a Python-based AI system that converts text into speech while adjusting the voice characteristics based on detected emotion.

The system analyzes the sentiment of the input text and dynamically modifies speech parameters such as rate and volume to produce more expressive and human-like audio output.

## Features

* Text input from user
* Emotion detection using VADER sentiment analysis
* Voice modulation based on emotion
* Audio file generation (.wav)

## Supported Emotions

* Happy
* Frustrated
* Neutral

## Technologies Used

* Python
* VADER Sentiment Analysis
* pyttsx3 (Text-to-Speech)
* Flask (optional for web interface)

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the Project

python main.py

## Example

Input:
I am very happy today!

Detected Emotion:
happy

Output:
Audio file generated as output.wav
