
dataneed = {
    "text" : "this is a sentence and its all the text in the audio file",
    "utterances":[
      {
        "confidence":0.9055882758620691,
        "end":32000,
        "speaker":"A",
        "start":0,
        "text":"Ted talks are recorded live at Ted conference.",
        "words":[
            {
               "text":"Ted",
               "start":8562,
               "end":8772,
               "confidence":0.75,
               "speaker":"A"
            },
            {
               "text":"talks",
               "start":8817,
               "end":9132,
               "confidence":0.99742,
               "speaker":"A"
            }
         ]
      },
          {
        "confidence":0.9055882758620691,
        "end":60000,
        "speaker":"B",
        "start":32001,
        "text":"Ted talks are recorded live at Ted conference.",
        "words":[
            {
               "text":"Ted",
               "start":8562,
               "end":8772,
               "confidence":0.75,
               "speaker":"A"
            },
            {
               "text":"talks",
               "start":8817,
               "end":9132,
               "confidence":0.99742,
               "speaker":"A"
            }
         ]
      },
      {
        "confidence":0.9055882758620691,
        "end":32000,
        "speaker":"C",
        "start":0,
        "text":"Ted talks are recorded live at Ted conference.",
        "words":[
            {
               "text":"Ted",
               "start":8562,
               "end":8772,
               "confidence":0.75,
               "speaker":"A"
            },
            {
               "text":"talks",
               "start":8817,
               "end":9132,
               "confidence":0.99742,
               "speaker":"A"
            }
         ]
      }
      ],
      "audio_duration": 60000
    }

from SpeakerDiarization import *
import numpy as np
from itertools import islice
import collections

#dataneed = SpeakerDiarization(audio="") #this is where speaker diarization is called

transcription = dataneed["text"]
diarization = dataneed["utterances"]
audiolength = int(dataneed["audio_duration"]/1000)

#time start and end in millieseconds -> convert to seconds
audiotexts = []
speakersvale = []
count = 0
for a in diarization:
    data = a
    speaker = data["speaker"]
    starttime = int(data["start"]/1000) #convert to seconds
    endtime = int(data["end"]/1000) #convert to seconds
    speech = data["text"]
    duraction = list(range(starttime,endtime))
    
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
    speakersvale.append(speaker)

#used when 
def listdupes(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    print(list(seen_twice))
    return list(seen_twice)

#listdupes(speakersvale)

def chunkgeneratory2(iterable, chunk_size):
    return [iterable[x:x + chunk_size] for x in range(0, len(iterable), chunk_size)]

def chunkgeneratory1(iterable, chunk_size):
    imagesList = iter(iterable)
    chunk = list(islice(imagesList, chunk_size)) #n is steps iterable is sliced
    while chunk:
        yield chunk
        chunk = list(islice(imagesList, chunk_size))

timetotal = list(range(0,audiolength+1))


def whoistalking():
    it = chunkgeneratory2(timetotal, 5)
    for dict_item in audiotexts:
            newdur = dict_item["duration"]
            it2 = chunkgeneratory1(newdur, 5)
            
            # while True:
            for yawn in it:
                try:
                    dur = yawn
                    dur2 = next(it2)
                except StopIteration:
                    break
                if collections.Counter(dur) == collections.Counter(dur2):
                    valt = "speaking"
                else:
                    valt = "silence"
                
                yield dict_item["speaker"],valt





def convertdict(): #returns speaker sequence
    isIT ={}
    speechsequeen = []
    donemaybe = whoistalking()        
    while True:
        try:
            letter = next(donemaybe)
        except StopIteration:
            break
        speechsequeen.append(letter)
    for x,y in speechsequeen:
        isIT.setdefault(x,[]).append(y)
    return isIT

#huh = convertdict(speechsequeen,isIT)
#print(huh) # this is a dictionary like this

#{'A': ['speaking', 'speaking', 'speaking', 'speaking', 'speaking', 'speaking', 'silence'], 
# 'B': ['silence', 'silence', 'silence', 'silence', 'silence', 'silence']}

print(convertdict())
