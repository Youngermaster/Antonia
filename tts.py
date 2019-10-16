from gtts import gTTS # Library to convert text to audio or speech.
import json # Library to load the json.
from translate import Translator # Library to Translate.
from PIL import Image
import random
import sys

ANSWER_PATH = "/home/pi/answer/answer.mp3"

class Tts:
    def translate(self, respuesta):
        translator = Translator(from_lang="english", to_lang="spanish")
        palabra = translator.translate(respuesta)
        return palabra

    def __init__(self):
        # List to search someone of the following words in the answer and show a related image.
        lista = [
        "arepa",
        "audio guide",
        "bakery pastery"
        "bandeja paisa",
        "bike tour",
        "brand coffe",
        "chiva tour",
        "coffe crop coffe cultivation",
        "coffe experience",
        "coffe tasting",
        "coffe tour",
        "echange languajes",
        "fruit vegetable",
        "gastronomy comuna 13",
        ]
        # We extract the information that we need from the cloud configuration file.
        # In this case we are using the text that we need to speech.    
        with open('config/cloud.json') as json_file:
            data = json.load(json_file)

            # We store the digital assistant answer.
            respuesta = data['text']

            # We get the STT initial query to show a related image.
            texto = data['channelExtensions']['debugInfo']['variables']['iResult']['query']

        # We extract the query initial language from lang configuration file.
        with open('config/lang.json') as json_file:
            data = json.load(json_file)
            languaje = data["lang"][0]

        if languaje == "esp":
            lang = "es"
            print("* DEBUG: START PY TTS *")
            # We store the final text in the right language.
            respuestafinal = self.translate(sys.argv[1])
        else:
            lang="en"
            repuestafinal = respuesta
        try:
            myobj=gTTS(text=respuestafinal,lang=lang)
            # We convert the final text on audio.
            myobj.save(ANSWER_PATH)
            print("* PYTHON DEBUG: END PY TTS *")

        except Exception as e: print(e)


Tts()
