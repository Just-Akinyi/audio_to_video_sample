from SpeakerDiarization import *
import numpy as np

dataneed = SpeakerDiarization(audio="") #needs audio url

transcription = dataneed["text"]
diarization = dataneed["utterances"]
audiolength = dataneed["audio_duration"]

#time start and end in millieseconds -> convert to seconds
audiotexts = [] #list of dictionaires


count = 0
for a in diarization:
    data = a
    speaker = data["speaker"]
    starttime = int(data["start"]/1000) #convert to seconds
    endtime = int(data["end"]/1000) #convert to seconds
    speech = data["text"]
    duraction = list(range(starttime,endtime))
    #duraction = np.arange(starttime,endtime+1,0.001)
    
    text = {
        "speaker" : speaker,
        # "start" : starttime, 
        # "end" : endtime,
        "duration" : duraction,
        "speech" : speech,
        "index" : count,
    }
    count += 1
    audiotexts.append(text)

print(audiotexts)

