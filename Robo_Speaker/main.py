import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print('Welcome to RoboSpeaker 1.1. Created by Sunil')

    while True:
        x = input("Enter what you want me to speak: ")
        if x == 'q':
            text_to_speech("Bye Bye Friend")
            break
        text_to_speech(x)


