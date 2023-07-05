# Generative_Pre-trained_Transformer
A project that uses the GPT language model to generate voice based on trends detected by a voice recognition program.
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def user_Command():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Something went wrong"

while True:
    print("Listening....")
    query = user_Command()

    websites = [["Youtube","https://www.youtube.com"],["Facebook", "https://www.facebook.com"],["google","https://www.google.com"]]
    for website in websites:
        if f"Open {website[0]}".lower() in query.lower():
            speaker.speak(f"Opening {website[0]}")
            webbrowser.open(website[1])
    if "open videos" in query:
        path = "C:\sidhanta prasad tripathy\data science videos"
        speaker.speak(query)
        os.system(path)
