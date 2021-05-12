import speech_recognition as sr
print("Bhauk!!")

recon = sr.Recognizer()

with sr.Microphone() as source:
    audio_text = recon.listen(source)
    print("Bas aur mat bhauk!")    
    try:
        print("Text: "+recon.recognize_google(audio_text))
    except:
         print("Kya bhauka")
