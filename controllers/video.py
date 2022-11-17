import os
from pathlib import Path


class Video:

    def __init__(self, format, bg_id, root_dir: Path) -> None:
        self.format = format
        self.bg_path = self.generate_bg_path(bg_id, root_dir)

    def generate_bg_path(self, id: str, root_dir) -> Path:
        for file in os.scandir(root_dir):
            if file.is_dir() and str(file.name).endswith(id):
                return Path(file.path)