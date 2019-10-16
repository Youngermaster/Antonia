import json # This library make us able to convert text to json.
import os # This library make us be able to execute Os commands

jsonStructure = {
    "user": "Antonia",
}

def get_string(request):
    return request

def generate_json():
    jsonStructure["text"] = get_string("Where can i see a tango show?")
    with open('json/request.json', 'w') as outfile:
        json.dump(jsonStructure, outfile)

def execute_curl(jsonName, tunnelUrl):
    os.system('curl -H "Content-Type: application/json" -d @json/' + jsonName + ' ' + tunnelUrl)

def core():
    generate_json()
    execute_curl('request.json', 'https://projectantonia.ngrok.io/test/message')

if __name__ == "__main__":
    core()