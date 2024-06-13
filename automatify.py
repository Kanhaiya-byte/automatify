# import cv2
# from flask import Flask, make_response, request, render_template, redirect,url_for,jsonify
# import io
# # from PIL import Image
# import numpy as np
# from pytesseract import pytesseract
# import os
# import speech_recognition as sr
# from tkinter import Image, filedialog
# import tkinter as tk
# import sys
from cgitb import text
from flask import Flask, make_response, request, render_template, redirect, jsonify
from googletrans import Translator
import re
import io
import googletrans
import numpy as np
import cv2  # Import OpenCV (cv2)
from pytesseract import pytesseract
import os
import speech_recognition as sr
from tkinter import Image, filedialog
import tkinter as tk
import sys
print(sys.path)

automatify = Flask(__name__)
# Set up the Translator
translator = googletrans.Translator()

automatify.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# main.hmtl ko link krdye hai routing or url se
@automatify.route("/main")
def main():
    return render_template("main.html")


# Home page
@automatify.route("/")
def home():
    return render_template("home.html")



# Image2text code
class OCR:
    def __init__(self, tesseract_path=None):
        if tesseract_path is not None:
            self.path = tesseract_path
        else:
            self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def extract(self, image_file):
        try:
            pytesseract.tesseract_cmd = self.path
            image_data = image_file.read()

            # Use OpenCV to read the image
            image = cv2.imdecode(np.frombuffer(image_data, np.uint8), -1)

            # Perform OCR on the image
            text = pytesseract.image_to_string(image)

            return text.strip()
        except Exception as e:
            # Log the error for debugging
            automatify.logger.error("Error during OCR: %s", repr(e))
            return "Error during OCR: {}".format(str(e))

@automatify.route("/Image2Text", methods=["GET", "POST"])
def index():
    extracted_text = ""  # Initialize with a default value

    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            ocr = OCR(tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe")
            extracted_text = ocr.extract(image_file)

    if extracted_text:
        return render_template("Image2Text.html", extracted_text=extracted_text)
    else:
        return render_template("Image2Text.html")








# Speech Recognition
@automatify.route('/SpeechRecognition')
def recog():
    return render_template('SpeechRecog.html')  # Update the template file name here

@automatify.route('/SpeechRecognition', methods=['POST'])
def speech_recognition():
    try:
        # Check if the 'audio' file was uploaded in the request
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file uploaded'})

        audio_file = request.files['audio']

        # Initialize the speech recognizer
        recognizer = sr.Recognizer()

        # Recognize speech from the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        # Perform speech recognition
        extracted_text = recognizer.recognize_google(audio_data)

        return render_template('SpeechRecog.html', extracted_text=extracted_text)
    except Exception as e:
        return jsonify({'error': str(e)})


# Translator
@automatify.route('/translate')
def trans():
  return render_template('translate.html')

@automatify.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    destination = request.form['destination']

    try:
        translation = translator.translate(text, dest=destination)

        if translation and translation.text:
            translated_text = translation.text
        else:
            translated_text = "Translation not available"
    except Exception as e:
        translated_text = f"Translation Error: {str(e)}"

    return render_template("translate.html", translation=translated_text)







# @automatify.route('/translate', methods=['POST'])
# def translate():
#     text = request.form['text']
#     destination = request.form['destination']

#     # List of supported destination languages
#     supported_languages = [
#         "afrikaans", "albanian", "amharic", "history", "arabic",
#         "armenian", "assamese", "aymara", "azerbaijani", "bambara",
#         "basque", "belarusian", "bengali", "bhojpuri", "bosnian",
#         "bulgarian", "catalan", "cebuano", "chichewa", "chinese-simplified",
#         "chinese-traditional", "corsican", "croatian", "czech", "danish",
#         "dhivehi", "dogri", "dutch", "english", "esperanto", "estonian",
#         "ewe", "filipino", "finnish", "french", "frisian", "galician",
#         "georgian", "german", "greek", "guarani", "gujarati", "haitian-creole",
#         "hausa", "hawaiian", "hebrew", "history-2", "hindi", "hmong",
#         "hungarian", "icelandic", "igbo", "ilocano", "indonesian", "irish",
#         "italian", "japanese", "javanese", "kannada", "kazakh", "khmer",
#         "kinyarwanda", "konkani", "korean", "krio", "kurdish-kurmanji",
#         "kurdish-sorani", "kyrgyz", "lao", "latin", "latvian", "lingala",
#         "lithuanian", "luganda", "luxembourgish", "macedonian", "maithili",
#         "malagasy", "malay", "malayalam", "maltese", "maori", "marathi",
#         "meiteilon", "mizo", "mongolian", "myanmar", "nepali", "norwegian",
#         "odia", "oromo", "pashto", "persian", "polish", "portuguese",
#         "punjabi", "quechua", "romanian", "russian", "samoan", "sanskrit",
#         "scots-gaelic", "sepedi", "serbian", "sesotho", "shona", "sindhi",
#         "sinhala", "slovak", "slovenian", "somali", "spanish", "sundanese",
#         "swahili", "swedish", "tajik", "tamil", "tatar", "telugu", "thai",
#         "tigrinya", "tsonga", "turkish", "turkmen", "twi", "ukrainian",
#         "urdu", "uyghur", "uzbek", "vietnamese", "welsh", "xhosa", "yiddish",
#         "yoruba", "zulu"
#     ]

#     if destination not in supported_languages:
#         return render_template("translate.html", translation="Invalid destination language")

#     try:
#         translation = translator.translate(text, dest=destination)

#         if translation and translation.text:
#             translated_text = translation.text
#         else:
#             translated_text = "Translation not available"
#     except Exception as e:
#         translated_text = f"Translation Error: {str(e)}"

#     return render_template("translate.html", translation=translated_text)







    
   

# For Refresh
@automatify.route("/", methods=["POST", "GET"])
def refresh():
    if request.method == "POST":
        return redirect("/")





if __name__ == "__main__":
    automatify.run(debug=True)


 















