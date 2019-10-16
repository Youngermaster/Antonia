import json # This library make us able to convert text to json.
import os # This library make us be able to execute Os commands

JSON_PATH = 'json/request.json'

# This will be the json to send to the server.
jsonTest = {
    "user": "Antonia",
}

# This method gets the request from the user.
def get_request(request):
    return request

def add_atributes_to_json():
    jsonTest["text"] = get_request("Where can i see a tango show?")

def generate_json():
    with open(JSON_PATH, 'w') as outfile:
        json.dump(jsonTest, outfile)

def execute_curl(jsonName, tunnelUrl):
    os.system('curl -H "Content-Type: application/json" -d @json/' + jsonName + ' ' + tunnelUrl)

def core():
    add_atributes_to_json()
    generate_json()
    execute_curl('request.json', 'https://projectantonia.ngrok.io/test/message')

if __name__ == "__main__":
    core()