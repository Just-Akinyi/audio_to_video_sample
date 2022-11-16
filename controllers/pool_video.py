from moviepy.editor import VideoFileClip, concatenate_videoclips

import os



#we use VideoFileClip() class create two video object, then we will merge them.


#Merge videos with concatenate_videoclips()




def pool(video_paths: list, out_path):

    videos = [VideoFileClip(path) for path in video_paths]

    final_video= concatenate_videoclips(videos, method='compose')
    
    final_video.write_videofile(out_path)
    for file in video_paths:
        os.remove(file)
    return out_path
