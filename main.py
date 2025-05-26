import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
engine=pyttsx3.init()
api_key='pub_880170b14316e2369b1811d374fae4aafedaf&q=India&country=in&language=en&category=politics'
url='https://newsdata.io/api/1/news?apikey='
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    genai.configure(api_key="AIzaSyAsg8dJwRe32SEglWL-R7pGhl8CWS38MBo")
    # Initialize the Gemini model (flash version for faster responses)
    model = genai.GenerativeModel("gemini-1.5-flash")

# Send a message similar to chat completions
    response = model.generate_content([
    {"role": "user", "parts": [command]}
    ])
    return response.text

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        response=requests.get(f'{url}+{api_key}')
        if response.status_code==200:
            data=response.json()
            results=data.get('results',[])
            for article in results:
                speak(article['title'])
                print(article['title'])
    else:
        output=aiProcess(c)
        print(output)
        speak(output)

       
        
        
    
if __name__=="__main__":
    speak("Initalizing Jarvis")
    while True:
        
    #listen for the wake word "Jarvis"
    #obtain audio from the microphone
      r =sr.Recognizer()
      try:
            with sr.Microphone() as source:
             print("Listening")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="hello"):
                print('Ya')
                speak('Ya')
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)

      except Exception as e:
            print("error: {0}".format(e))
    
   