import ffmpeg
import json
import time
from uuid import uuid4
# from ffmpeg import stream

""" split_wav `audio file` `time listing`
    `audio file` is any file known by local FFmpeg
    `time listing` is a file containing multiple lines of format:
        `start time` `end time` output name 
    times can be either MM:SS or S*
"""


class AudioSplit:

    def __init__(self, speaker, start, end, index) -> None:
        self.speaker  = speaker
        self.start = start
        self.end = end
        self.index = index
        self._stream =None
        self.transcription = None
        self.video = None

    @property
    def start_seconds(self):
        minute, sec = map(int, self.start.split(':'))
        total_time = (minute * 60) + sec
        return total_time


    @property
    def duration(self):
        minute, sec = map(int, self.end.split(':'))
        total_time = (minute * 60) + sec
        duration = total_time - self.start_seconds
        return duration

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, input_audio):
        self._stream = input_audio

    def __repr__(self) -> str:
        return f"""SPEAKER: <{self.speaker}>, 
        START: <{self.start_seconds}>, 
        DURATION: <{self.duration}>, 
        STREAM: <{self.stream}>, 
        TRANSCRIPTION: <{self.transcription}>
        VIDEO: <{self.video}>"""



def make_time(elem: str):
    # allow user to enter times on CLI
    t = elem.split('-')
    try:
        # will fail if no ':' in time, otherwise add together for total seconds
        return int(t[0]) * 60 + float(t[1])
    except IndexError:
        return float(t[0])


def collect_from_file(time_stamp_path) -> list[AudioSplit]:
    """user can save times in a file, with start and end time on a line"""
    time_pairs = []
    with open(time_stamp_path) as in_times:
        times_db = json.load(in_times)
        # number_speakers = times_db["number_of_speakers"]
        diarize_parser = times_db["diarization"]
        for _id in diarize_parser:
            start, end = diarize_parser[_id][1].split('-')
            time_pairs.append(
                AudioSplit(
                    diarize_parser[_id][0], 
                    start=start, end=end, 
                    index=_id
                )
            )
    return time_pairs


def segment_audiofile(audio_path, time_stamp_path):
    
    _in_file = audio_path
    audios = []
    for audio_split in collect_from_file(time_stamp_path):
        # open a file, from `ss`, for duration `t`
        stream = ffmpeg.input(_in_file, ss=audio_split.start_seconds, t=audio_split.duration)
        path = f'data/temp_data/{uuid4()}.wav'
        try:
            stream = ffmpeg.output(stream, path, format='wav')
            audio_split._stream = path
            audios.append(audio_split)
            
            ffmpeg.run(stream)
           
        except ffmpeg.Error as e:
            print("output")
            print(e.stdout)
            print("err")
            print(e.stderr)

    return audios



