import os
from pathlib import Path



class Speaker:

    def __init__(self, id: str, root_dir) -> None:
        self.dir_path = self.generate_avatar_path(id, root_dir)
        self.sequence = []
        
        
    def generate_avatar_path(self, id: str, root_dir) -> Path:
        # directory = DATA_DIR / "Image/avatars"
        for file in os.scandir(root_dir):
            if file.is_dir() and str(file.name).endswith(id):
                return Path(file.path)

    def generate_animation_sequence(self, sequence_dict: dict, total_len: int):
        for sec in range(total_len):
            if total_len != 0:
                for timestamp in sequence_dict:
                    if sec in sequence_dict[timestamp][1]:
                        self.sequence.append(sequence_dict[timestamp][0])
                total_len -= 1


    def __repr__(self) -> str:
        return f"""DIR_PATH: <{self.dir_path}>,
                   SEQUENCE: <{self.sequence}>
        """
        