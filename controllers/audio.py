from pathlib import Path

class Audio:

    def __init__(self, format, length, num_speakers, path: str) -> None:
        self.format = format
        self.lenght = length
        self.num_speakers = num_speakers
        self.path = Path() / path


    def __repr__(self) -> str:
        return f"FORMAT: <{self.format}>\nLENGTH: <{self.lenght}>\nNUM_SPEAKERS: <{self.num_speakers}>\nPATH: <{self.path}>\n"