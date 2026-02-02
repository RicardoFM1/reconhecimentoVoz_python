import speech_recognition as sr
import time
import webbrowser

reconhecimento = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo legal:")
    audio = reconhecimento.listen(source)

try: 
    texto = reconhecimento.recognize_google(audio, language='pt-BR')
    print("Você disse:", texto)
    if "navegador" in texto.lower() or "google" in texto.lower():
        for i in range(3):
            print("Abrindo navegador...")
            time.sleep(1)
        webbrowser.open('https://google.com')
        print("Navegador aberto!")
    elif "youtube" in texto.lower():
        time.sleep(1)
        webbrowser.open_new_tab("https://www.youtube.com")
except sr.UnknownValueError:
    print("Não entendi o que quis dizer, tente novamente!")
