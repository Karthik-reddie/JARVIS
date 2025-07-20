import pyttsx3
def speak(text):
    engine=pyttsx3.init()
    pitch=180
    rate=180
    volume=3
    voice_id=engine.getProperty("voices")

    if voice_id:
        voices=engine.getProperty("voices")
        try:
            engine.setProperty('voice',voices[3].id)
        except IndexError:
            print("Voice ID not found. Using the default voice")

    engine.setProperty('rate',rate) #speed of speech
    engine.setProperty('volume',volume) #volume level (0.0 to 1.0)
    engine.setProperty('pitch',pitch)  #pitch level (0 to 100)


    print(text)
    engine.say(text)
    engine.runAndWait()


# speak(text)