import json

class Speaker:

    def __init__(self, speaker, start, end, index, transcription) -> None:
        self.speaker  = speaker
        self.start = start
        self.end = end
        self.index = index
        self.transcription = transcription
        self.video = None
        self.is_active = False


    @property
    def coordinate(self):
        if self.speaker == 'speaker_1':
            return(150, 50)   
        elif self.speaker == 'speaker_2':
            return(150, 300)

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


def collect_from_file(time_stamp_path) -> list[Speaker]:
    """user can save times in a file, with start and end time on a line"""
    video_map = []
    with open(time_stamp_path) as in_times:
        times_db = json.load(in_times)
        avatars = times_db["avatar_paths"]
        diarize_parser = times_db["diarization"]
        for _id in diarize_parser:
            start, end = diarize_parser[_id][1].split('-')
            video_map.append(
                Speaker(
                    diarize_parser[_id][0], 
                    start=start, end=end, 
                    index=_id,
                    transcription = diarize_parser[_id][2]
                )
            )
    return video_map, avatars


# def segment_audiofile(audio_path, time_stamp_path):
    
#     _in_file = audio_path
#     audios = []
#     for audio_split in collect_from_file(time_stamp_path):
#         # open a file, from `ss`, for duration `t`
#         stream = ffmpeg.input(_in_file, ss=audio_split.start_seconds, t=audio_split.duration)
#         path = f'data/temp_data/{uuid4()}.wav'
#         try:
#             stream = ffmpeg.output(stream, path, format='wav')
#             audio_split._stream = path
#             audios.append(audio_split)
            
#             ffmpeg.run(stream)
           
#         except ffmpeg.Error as e:
#             print("output")
#             print(e.stdout)
#             print("err")
#             print(e.stderr)

#     return audios



