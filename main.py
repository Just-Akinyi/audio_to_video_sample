# from collections import deque
import time
from controllers.serializer import load_data
from controllers.animator import generate_animation
from controllers.pool_video import pool

from moviepy.editor import VideoFileClip, AudioFileClip
import os
from sys import argv
from pathlib import Path
from uuid import uuid4








ROOT_DIR = Path(__file__).parent.resolve()
DATA_DIR = Path(ROOT_DIR) / "data"
# @click.group()
# def cli():
#     pass


# @click.command()
# @click.argument('-M', '--metadata_json', description='path to metadata json format')
# @click.argument('-A', '--audio_path', description='path to audio file')
# @click.argument('-O', '--output_path', description='path to video output')
# def animate(metadata_json: str, audio_path: str, output_path: str) -> None:
def animate( metadata_path :str) -> None:
    """_summary_

    Args:
        metadata_json (str): _description_
        audio_path (str): _description_
        output_path (str): _description_
    """
    output_path = f'data/Result/{str(uuid4())}.mp4'


    audio_obj, video_obj, animation_data = load_data(metadata_path, data_dir=DATA_DIR)
    for dt in animation_data:
        print(dt)

    animation_path = generate_animation(animation_data, video_obj.bg_path, audio_obj.num_speakers)
    videoclip = VideoFileClip(animation_path)
    audioclip = AudioFileClip(audio_obj.path)
    video = videoclip.set_audio(audioclip)
    video.write_videofile(output_path)
    print(f'YOUR VIDEO HAS BEEN SAVED TO: [{output_path}]')
    



# registering the commands
if __name__=='__main__':
    # cli.add_command(animate)
    # cli()
    start = time.time()
    metadata_path = str(argv[1])
    animate(metadata_path)
    # animate("data/Audio/Recording.m4a", 'timestamp.json')
    print(f'RUNTIME: [{time.time() - start}]')
    