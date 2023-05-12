import speech_recognition as sr
from pydub import AudioSegment

# cargar el archivo de audio
audio_file = AudioSegment.from_wav(r'C:\Users\Cyber\Desktop\emociones\llamada\llamada_completa_2.wav')

# establecer la duración máxima del segmento de audio en segundos
max_segment_duration = 10

# calcular la cantidad total de segmentos de audio
total_segments = (len(audio_file) // (max_segment_duration * 1000)) + 1

# transcribir cada segmento de audio
transcription = ''
for i in range(total_segments):
    # definir los tiempos de inicio y fin del segmento de audio
    start = i * max_segment_duration * 1000
    end = start + max_segment_duration * 1000
    
    # cortar el segmento de audio
    audio_segment = audio_file[start:end]
    
    # convertir el segmento de audio a formato compatible con SpeechRecognition
    audio = sr.AudioData(audio_segment.raw_data, audio_segment.frame_rate, audio_segment.sample_width)
    
    # transcribir el audio
    r = sr.Recognizer()
    text = r.recognize_google(audio, language='es-MX')
    
    # agregar la transcripción del segmento al texto completo
    transcription += text

# guardar la transcripción en un archivo de texto
with open(r'C:\Users\Cyber\Desktop\emociones\oficial\llamada_text.txt', 'w') as file:
    file.write(transcription)
