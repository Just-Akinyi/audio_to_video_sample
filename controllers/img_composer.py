import cv2
from uuid import uuid4
from .serializer import Speaker
from .create_image import make_image

FRAMES = 24
BACKGROUND = 'data/Image/Team-Clutch-03.png'


def get_image(speaker: str):
    return cv2.imread(f'data/Image/{speaker}.jpg')


def make_video(
    speaker: str,
    duration: int,
    transcription: str,
    coordinate: tuple[int, int], 
    avatars: dict[str, str] ):

    
    images = []
    output = f'data/compiled_videos/{str(uuid4())}.mp4'
    duration = duration
    video_text = transcription.split()
    
    len_per_word = duration / len(video_text)
    for text in video_text:
        temp_imgs = [
            make_image(
                avatars, speaker, 
                coordinate, BACKGROUND,  
                text=text
                ) for _ in range(int(len_per_word * FRAMES))
                ]
        images.extend(temp_imgs)
    # images = [get_image(speaker) for _ in range(int(int(duration) * FRAMES))]
    frame_one = images[0]
    height, width, _ = frame_one.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(output, fourcc, 24.0, (width, height))

    for image in images:
        out.write(image) # Write out frame to video
        

        # cv2.imshow('video',frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
            break

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
    return output

