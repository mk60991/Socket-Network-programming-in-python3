import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('say somethiong')
    audio=r.listen(source)
    
try:
    print('google thinks you said:\n'+r.recognize_google(audio))
    
except:
    pass
