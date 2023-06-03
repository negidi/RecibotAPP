import speech_recognition as sr
from gtts import gTTS
import playsound
import tempfile
import os

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language="es-ES")
        print("Has dicho:", text)
        return text
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print("Error al realizar la solicitud: {0}".format(e))

def speak(text):
    tts = gTTS(text=text, lang="es")
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(fp.name + ".mp3")
        playsound.playsound(fp.name + ".mp3", True)
    os.remove(fp.name + ".mp3")

def train_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Entrenando voz...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    try:
        print("Entrenamiento completado.")
        return audio
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio de entrenamiento.")
    except sr.RequestError as e:
        print("Error al realizar la solicitud: {0}".format(e))

def main():
    # Entrenar el modelo de reconocimiento de voz con tu voz
    trained_audio = train_voice()
    if trained_audio is None:
        print("No se pudo entrenar el modelo de voz. Saliendo...")
        return
    
    speak("¡Hola! me llamo recibot ¿En qué puedo ayudarte hoy?")
    while True:
        text = listen()
        if text is None:
            continue  # Vuelve a escuchar si no se detecta ninguna entrada de voz

        if text == "adiós":
            speak("¡Hasta luego!")
            break
        # Lógica del asistente virtual para responder a preguntas
        if "que son los residuos inorganicos" in text:
            response = "Los residuos inorgánicos agrupan a todos los residuos que no tienen procedencia biológica. En cambio, su origen emana de forma artificial. Se trata de residuos no biodegradables que no logran reintegrarse al ecosistema naturalmente. Si lo hacen, emiten sustancias nocivas al medio ambiente."
        if "dónde reciclar" in text:
            response = "los robots dominaran el mundo"
            speak(response)
      
        else:
            speak("Lo siento, no entendí tu pregunta. ¿Puedes repetirla?")
            
if __name__ == "__main__":
    main()
