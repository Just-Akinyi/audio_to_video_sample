import speech_recognition as sr
import eng_to_ipa  as ipa
import time

def phonology_list(sentence: str) -> list[list[str] | str]:
    result =  ipa.ipa_list(sentence)
    return result


def transcribe(audio_path: str):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)  # read the entire audio file            
        transcript =  r.recognize_google(audio)
        
        return phonology_list(transcript)

# start = time.time()
# transcribe('data/temp_data/c0e8a890-1372-43bf-b69a-a92d48be3f00.wav')
# print(f'RUNTIME: [{time.time() - start}]')