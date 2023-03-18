import openai
import pyaudio
import wave


def record_voice(wave_output_file, record_seconds=10):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 2**11

    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    frames = []

    for _ in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(wave_output_file, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))


def wave_to_text(audio_file, api_key_path="api.key")

openai.api_key_path = "api.key"
audio_file = open("sample.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)

# %%
transcript.text
# %%
# %%
