import os
from pathlib import Path


class Video:

    def __init__(self, format, bg_id, root_dir: Path) -> None:
        self.format = format
        self.bg_path = root_dir / "background_01.png"
        
    #     self.generate_bg_path(bg_id, root_dir)

    # def generate_bg_path(self, id: str, root_dir: Path) -> Path:
    #     print(root_dir)
    #     for file in os.scandir(root_dir):
    #         if file.is_file() and str(file.name).endswith(id):
    #             print(file.path)
    #             return Path(file.path)