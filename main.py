import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    

if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        #Listen for the wake eord "Jarvis"
        #Obtain audio from the microphone
        r = sr.Recognizer()
        

        # recogize speech using Google Speech Recognition
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listenning...")
                audio = r.listen(source)#,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("welcome sir")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvic active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
                     

        except Exception as e:
            print("Error;{0}".format(e))
            # speak("Sorry, I didn't understand that. Please try again.")