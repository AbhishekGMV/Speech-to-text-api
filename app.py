from flask import Flask, request, jsonify
import speech_recognition as sr
from os import path
app = Flask(__name__)

@app.route('/')
def index():
    print(sr.__version__)
    return "<h3>Make a post request to <uri>/transcribeAudio, with an audio file(.wav) for transcription</h3>"

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


if __name__ == '__main__':
    app.run(debug=True)



