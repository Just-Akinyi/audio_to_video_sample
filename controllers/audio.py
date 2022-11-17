from pathlib import Path

class Audio:

    def __init__(self, format, length, num_speakers, path: str) -> None:
        self.format = format
        self.lenght = length
        self.num_speakers = num_speakers
        self.path = Path() / path