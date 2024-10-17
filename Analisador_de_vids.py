from pytube import Youtube
import ffmpeg;
import openai;

def download_audio(url):
    yt= Youtube(url)
    audio_stream= yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='audio.mpp4')

def converter_audio():
    stream = ffmpeg.input('audio.mp4')
    stream = ffmpeg.output(stream, 'audio.wav')
    ffmpeg.run(stream)

openai.api_key = 'YOUR_OPENAI_API_KEY'

def transcrever_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file
        )
    return transcript['text']

def resumir_texto(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Resuma o seguinte texto: {text}",
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return summary

def main(url):
    download_audio(url)
    converter_audio()
    transcript = transcrever_audio("audio.wav")
    summary = resumir_texto(transcript)
    print("Summary:", summary)

if __name__ == "__main__":
    url = "URL_DO_VIDEO_AQUI"
    main(url)
