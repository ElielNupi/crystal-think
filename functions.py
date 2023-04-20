import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import time
from get_env import print_env
import openai

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say("Iniciando Sistema...")
maquina.runAndWait()

#  configurando ambiente do chatGPT
env = print_env(['app_key'])
openai.api_key = env['app_key']
model_engine = 'text-davinci-003'

def listen_command():
    try:
        with sr.Microphone() as source:
            maquina.say("Como posso te ajudar agora?")
            maquina.runAndWait()
            print("Como posso te ajudar?")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            
            if 'cristal' in comando:
                comando = comando.replace('cristal','')
                # maquina.say(comando)
                maquina.runAndWait()
                
            elif 'cristal' not in comando:
                pass
    except Exception as error: 
        print(f'Um erro ocorreu: {error}')

    return comando

def execute_command():
    comando  = listen_command()
    if 'wikipedia' in comando :
        src = comando.replace('wikipedia', '')
        wikipedia.set_lang('pt')
        result = wikipedia.summary(src,2)
        print(result)
        maquina.say(f"Ok! Encontrei este resultado: {result}")
        time.sleep(3)
        maquina.say(result)
        maquina.runAndWait()

    elif 'toque' in comando or 'reproduza' in comando or 'toca' in comando:
        src = comando.replace('toque', '')
        src = comando.replace('reproduza', '')
        src = comando.replace('toca', '')
        result = pywhatkit.playonyt(src)

    else:
        prompt = comando
        completation = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5,
        )
        response = completation.choices[0].text
        print(response)
        maquina.say(response)
        maquina.runAndWait()