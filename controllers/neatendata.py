from SpeakerDiarization import *

dataneed = SpeakerDiarization(audio="") #needs audio file url

transcription = dataneed["text"]
diarization = dataneed["utterances"]
audiolength = dataneed["audio_duration"]

#time start and end in millieseconds -> convert to seconds
audiotexts = []

import numpy as np
count = 0
for a in diarization:
    data = a
    speaker = data["speaker"]
    starttime = data["start"]/1000.0 #convert to seconds
    endtime = data["end"]/1000.0 #convert to seconds
    speech = data["text"]
    duraction = np.arange(starttime,endtime+1,0.001)
    
    text = {
        "speaker" : speaker,
        "start" : starttime, 
        "end" : endtime,
        "duration" : duraction,
        "speech" : speech,
        "index" : count,
    }
    count += 1
    audiotexts.append(text)

