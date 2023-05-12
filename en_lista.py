import os
from google.cloud import speech
import subprocess

# Defina los nombres de archivo de entrada y salida
input_file = r'C:\Users\Cyber\Desktop\emociones\llamada\llamada_completa_2.wav'
output_file = r'C:\Users\Cyber\Desktop\emociones\llamada\llamada_completa_2_mono.wav'

# Ejecute el comando ffmpeg
subprocess.run(['ffmpeg', '-i', input_file, '-ac', '1', output_file])

# Cargue el archivo de audio de un solo canal en un objeto RecognitionAudio
with open(output_file, 'rb') as f:
    byte_data_mono = f.read()

audio_mono = speech.RecognitionAudio(content=byte_data_mono)

# Configure la configuración de reconocimiento para el archivo de audio de un solo canal
config_mono = speech.RecognitionConfig(
    sample_rate_hertz=8000,
    enable_automatic_punctuation=True,
    language_code='es-MX'
)


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\dgoogle\magnetic-rite-386519-174ddc1eb665.json'
speech_client = speech.SpeechClient()

# Example 1 & 2. Transcribe Local Media File 
# File Size: < 10mbs, length < 1 minute

## Step 1. Load the media files

media_file_name_wav = r'C:\Users\Cyber\Desktop\emociones\llamada\llamada_completa_2.wav'


with open(media_file_name_wav, 'rb') as f2:
    byte_data_wav = f2.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

## Step 2. Configure Media Files Output
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=8000,
    enable_automatic_punctuation=True,
    language_code='es-MX'
)

config_wav = speech.RecognitionConfig(
    sample_rate_hertz=8000,
    enable_automatic_punctuation=True,
    language_code='es-MX',
    audio_channel_count=2
)

## Step 3. Transcribing the RecognitionAudio objects
response_standard_wav = speech_client.recognize(
    config=config_wav,
    audio=audio_wav
)

print(response_standard_wav)


# Example 3: Transcribing a long media file
media_uri = 'gs://llamada_completa_2/llamada_completa_2.wav'
long_audi_wav = speech.RecognitionAudio(uri=media_uri)

config_wav_enhanced = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='es-MX',
    use_enhanced=True,
    model='video'
)

operation = speech_client.long_running_recognize(
    config=config_wav,
    audio=long_audi_wav
)
response = operation.result(timeout=90)
print(response)

for result in response.results:
    print(result.alternatives[0].transcript)
    print(result.alternatives[0].confidence)
    print()

# Transcriba el archivo de audio de un solo canal
response_mono = speech_client.recognize(
    config=config_mono,
    audio=audio_mono
)

# Imprima la transcripción
for result in response_mono.results:
    print(result.alternatives[0].transcript)