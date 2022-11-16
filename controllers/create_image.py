from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
import numpy as np


FONT = ImageFont.truetype('data/Fonts/arial.ttf', 100)


def draw_text(img: Image, text: str, coordinate: tuple[int]) -> Image:
    drawer = ImageDraw.Draw(img)
    drawer.text(coordinate, text,  font=FONT )


def make_image(
    avatars: dict[str, str], 
    speaker,
    coordinate,
    background_path: str, 
    text: str
) -> Image:
    background_image = Image.open(background_path)
    background_image = background_image.convert(mode='RGBA')
    width, length = background_image.size
    canvas = Image.new(mode='RGBA', size=(width, length), color=(255, 255, 255))
    canvas.paste(im=background_image, box=(0,0))
    for avatar in avatars:
        speaker_state = Image.open(avatar)
        speaker_state = speaker_state.convert('RGBA')
        if avatars[avatar] == speaker:
            draw_text(speaker_state, text, coordinate)
        canvas = Image.alpha_composite(canvas, speaker_state)
    numpy_img = np.array(canvas)
    cv2_image = cv.cvtColor(numpy_img, cv.COLOR_RGB2BGR)
    return cv2_image
    
