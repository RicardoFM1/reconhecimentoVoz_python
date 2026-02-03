import speech_recognition as sr
import time
import webbrowser

reconhecimento = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo legal:")
    audio = reconhecimento.listen(source)

try:
   
    texto = reconhecimento.recognize_google(audio, language="pt-BR")
    print("Você disse:", texto)

   
    texto_pesquisa = texto.lower()

    palavras_remover = ["google", "navegador", "youtube"]

    for palavra in palavras_remover:
        texto_pesquisa = texto_pesquisa.replace(palavra, "")

    texto_pesquisa = texto_pesquisa.strip()

    if "navegador" in texto.lower() or "google" in texto.lower():
        print("Abrindo navegador...")
        time.sleep(1)
        webbrowser.open(
            "https://google.com/search?q=" + texto_pesquisa
        )

    elif "youtube" in texto.lower():
        print("Abrindo YouTube...")
        time.sleep(1)
        webbrowser.open_new_tab(
            f"https://www.youtube.com/results?search_query={texto_pesquisa}"
        )

except sr.UnknownValueError:
    print("Não entendi o que quis dizer, tente novamente!")
