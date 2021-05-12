import speech_recognition as sr
print("Bhauk!!")

r = sr.Recognizer()

with sr.Microphone() as source:
    audio_text = r.listen(source)
    print("Bas aur mat bhauk!")    
    try:
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Kya bhauka")