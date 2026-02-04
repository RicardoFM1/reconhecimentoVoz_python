from email.mime import audio
import speech_recognition as sr
import time
import tkinter as tk
import webbrowser

janela = tk.Tk()
janela.title("Assistente de Voz")

def processar_reconhecimento():
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
            labelStatus = tk.Label(janela, text="Abrindo navegador...")
            labelStatus.pack(pady=10)
            time.sleep(1)
            webbrowser.open(
                "https://google.com/search?q=" + texto_pesquisa
            )
            labelStatus.after(3000, labelStatus.destroy)

        elif "youtube" in texto.lower():
            print("Abrindo YouTube...")
            labelStatusYoutube = tk.Label(janela, text="Abrindo YouTube...")
            labelStatusYoutube.pack(pady=10)
            time.sleep(1)
            webbrowser.open_new_tab(
                f"https://www.youtube.com/results?search_query={texto_pesquisa}"
            )
            labelStatusYoutube.after(3000, labelStatusYoutube.destroy)

    except sr.UnknownValueError:
        print("Não entendi o que quis dizer, tente novamente!")



label = tk.Label(janela, text="Clique no botão e fale algo")
label.pack(pady=10)
button = tk.Button(janela, text="Falar", command=processar_reconhecimento)
button.pack(pady=10)

janela.mainloop()

