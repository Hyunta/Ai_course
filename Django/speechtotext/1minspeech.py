import os

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io



    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\mohai\\PycharmProjects\\speech-1608264784772-84096af9cdee.json'
transcribe_file('resources/file.wav')

