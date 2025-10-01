import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from google import genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

newsapi = "024bf56f716147049e0f1282fa821c67"

def aiprocess(command):
    client = genai.Client(api_key="AIzaSyDUmF9MaPne_Pv7f8l6ssTrdJKNhRhkWYo")
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents=[
           "You are a virtual assistant named jarvis skilled in general task like Alexa and Google Cloud. Always answer as brifely as possible, using no more than three sentences. ",
            command
       ], 
    )
    return response.text

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.in")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
    elif c.lower().startswith("play"):
        song = ' '.join(c.lower().split(" ")[1:])
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=024bf56f716147049e0f1282fa821c67")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
                print(article['title'])
    else:
        output = aiprocess(c)
        print(output)

        speak(output)

if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        #Obtain audio from the microphone
        r = sr.Recognizer()
        
        # recogize speech using Google Speech Recognition
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listenning...")
                audio = r.listen(source)#,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("welcome sir")
                #Listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)     
                    print("Jarvic active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
                     

        except Exception as e:
            print("Error;{0}".format(e))
            # speak("Sorry, I didn't understand that. Please try again.")