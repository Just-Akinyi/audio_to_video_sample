import cv2
import os
from pathlib import Path
from uuid import uuid4

FRAMES = 20.0


def get_image(speaker: str):
    return cv2.imread(f'data/Image/{speaker}.jpg')


def make_video(speaker: str, duration):
    output = f'data/compiled_videos/{str(uuid4())}.mp4'
    images = [get_image(speaker) for _ in range(int(int(duration) * FRAMES))]
    frame_one = images[0]
    height, width, channels = frame_one.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

    for image in images:
        out.write(image) # Write out frame to video
        

        # cv2.imshow('video',frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
            break

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
    return output

