from gtts import gTTS
from IPython.display import Audio
import speech_recognition as sr
from datetime import datetime
import webbrowser
import pyttsx3

engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

recognizer = sr.Recognizer()

def ouvir_comando():
    with sr.Microphone() as source:
        print("Ajustando o ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source)
        print("Por favor, fale algo:")
        
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")  
        print("Você disse: " + texto)
        return texto.lower()  
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")
        return None
    except sr.RequestError:
        print("Não foi possível conectar ao serviço de reconhecimento de fala.")
        return None

print("Olá, sou sua virtual assistent. Como deseja prossegir?\n")
print("Digite 1 para abrir o conversor de texto em fala ou 2 para o modo assistência básica.\n")

opcao = int(input()) 

if opcao == 1:
  
  print("Escreva um texto:\n")

  text_to_say = input()

  print("Escolha uma das opções de linguagem: inglês(en), francês (fr) ou Português (pt)")

  language = input()

  gtts_object = gTTS(text = text_to_say, lang = language, slow = False)

  gtts_object.save("conversao.wav")

  Audio("conversao.wav")

elif opcao == 2:
    loop = True

    while loop:
        comando = ouvir_comando()
        if comando:
            if "fechar" in comando:
                print("Programa encerrado.")
                falar("Programa encerrado.")
                loop = False 

            elif "vídeo" in comando:
                print("Abrindo o YouTube...")
                falar("Abrindo o YouTube.")
                webbrowser.open("https://www.youtube.com")  

            elif "wiki" in comando:
                print("Abrindo a Wikipedia...")
                falar("Abrindo a Wikipedia.")
                webbrowser.open("https://www.wikipedia.org") 

            elif "mapa" in comando:
                print("Abrindo o Google Maps...")
                falar("Abrindo o Google Maps.")
                webbrowser.open("https://www.google.com/maps") 
            
            elif 'tempo' in comando:
                strTime = datetime.today().strftime("%H:%M %p")
                print(strTime)
                falar(strTime)
    
            else:
                # Reproduz o texto em fala
                falar(comando)