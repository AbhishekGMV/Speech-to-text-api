from flask import Flask, request, jsonify
import speech_recognition as sr
from os import path
app = Flask(__name__)

@app.route('/')
def index(methods=['GET']):
    return "<h3>Make a post request with an audio file for transcription</h3>"

@app.route('/transcribeAudio', methods=['POST'])
def convertAudioFiletoText():
    AUDIO_FILE = request.files['audio']
    recognizer = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
        response = recognizer.recognize_google(audio, language='en-IN')
        json_response = jsonify({"responseText": response})
    return json_response
app.run()    
