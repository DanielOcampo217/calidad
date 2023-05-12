import io
import os
import soundfile as sf

import openai
import speech_recognition as sr
from google.cloud import speech_v1p1beta1 as speech

# configurar las credenciales de OpenAI
openai.api_key = "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"

# configurar las credenciales de Google Speech-to-Text
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\dgoogle\magnetic-rite-386519-174ddc1eb665.json"

# definir la ruta de tu archivo de audio
audio_file = r"C:\Users\Cyber\Desktop\emociones\llamada\llamada_completa_2.wav"

# obtener la duración del audio
with sr.AudioFile(audio_file) as source:
    duration = source.DURATION

# definir la duración máxima de cada segmento de audio
segment_duration = 10  # segundos

# inicializar la lista de transcripciones
transcripts = []

# dividir el audio en segmentos de duración definida
with sf.SoundFile(audio_file) as f:

    for i in range(0, int(duration), segment_duration):
        # obtener el segmento de audio
        start = i
        end = min(i + segment_duration, duration)
        f.seek(start * f.samplerate)
        audio_data = f.read(frames=(end-start) * f.samplerate, dtype='float32')
        bytes_per_sample = f.subtype.itemsize
        audio_segment = sr.AudioData(audio_data.tobytes(), f.samplerate, bytes_per_sample, subtype='PCM_' + str(f.subtype).split('.')[1])

        # transcribir el segmento de audio con OpenAI
        bytes_per_sample = f.subtype.itemsize
        bytes_per_channel = bytes_per_sample * f.channels
        audio_segment = sr.AudioData(audio_data.tobytes(), f.samplerate, bytes_per_channel)

        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Transcribe the following audio:\n{audio_segment}",
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        transcript = response.choices[0].text.strip()

        # si OpenAI no pudo transcribir el segmento de audio, intentar con Google Speech-to-Text
        if not transcript:
            client = speech.SpeechClient()
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=f.samplerate,
                language_code="es-MX",
                audio_channel_count=1,
                enable_word_time_offsets=True,
            )
            audio = speech.RecognitionAudio(content=audio_data)
            response = client.recognize(config=config, audio=audio)
            for result in response.results:
                for alternative in result.alternatives:
                    transcript += alternative.transcript

        transcripts.append(transcript)

# unir las transcripciones en un solo texto
text = "\n".join(transcripts)

# guardar la transcripción en un archivo de texto
with io.open(r"C:\Users\Cyber\Desktop\emociones\oficial\llamada_text.txt", "w", encoding="utf-8") as file:
    file.write(text)
