import json
from pathlib import Path
from .speaker import Speaker
from .audio import Audio
from .video import Video



def parse_timestamp(timestamp_dict: dict[str, list[str]]) -> None:
    for speech_frame in timestamp_dict:
        start, stop = speech_frame.split('-')
        start_time = extract_time(start)
        stop_time = extract_time(stop)
        time_range = [sec for sec in range(start_time, stop_time +1, 1)]
        timestamp_dict[speech_frame].append(time_range)


def extract_time(time: str):
    minute, sec = map(int, time.split(':'))
    total_time = (minute * 60) + sec
    return total_time



def load_data(file_path, data_dir: Path):
    """user can save times in a file, with start and end time on a line"""
    animation_data = []
    with open(file_path) as metadata_file:
        metadata = json.load(metadata_file)
        audio_data = metadata["audio"]
        audio = Audio(
            format = audio_data["format"],
            length= audio_data["length"],
            path = audio_data["path"],
            num_speakers= audio_data["number_speakers"]
        )
        video_data = metadata["output"]
        video = Video(
            format=video_data["format"],
            bg_id = video_data["background_id"],
            root_dir= data_dir / "Image/backgrounds"
            )
        diarization_data = metadata["diarization"]
        for speaker in diarization_data:
            avatar_id = speaker.split('_')[1]
            speaker_obj = Speaker(
                avatar_id,
                root_dir = data_dir / "Image/avatars"
                )
            parse_timestamp(diarization_data[speaker])
            speaker_obj.generate_animation_sequence(diarization_data[speaker], audio.lenght)
            animation_data.append(speaker_obj)

    return audio, video, animation_data


        


   








        
 
        


