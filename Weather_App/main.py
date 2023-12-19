import requests
import json
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print('Welcome to Weather App 1.1. Created by Sunil')

    while True:
        try:
            city = input("Enter the name of the city: ")
            url = f"https://api.weatherapi.com/v1/current.json?key=d551f70c23df4a3a84a163752231912&q={city}"
            if city == 'q':
                text_to_speech("Bye Bye Friend")
                break
            r = requests.get(url)
            wdic = json.loads(r.text)
            w = wdic["current"]["temp_c"]
            msg = f"The current weather in {city} is {w} degrees"
            print(msg)
            text_to_speech(msg)
        except:
            print(f"Please Enter Correct City Name")
            text_to_speech("Please Enter Correct City Name")