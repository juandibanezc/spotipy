from .files import JPEGFile
from .song import Song
from .episode import Episode
from typing import Union

class Spotipy:
    def __init__(self, name: str, duration_ms: int, file_path: str):
        self.name = name
        self.duration_ms = duration_ms
        self.image = JPEGFile(file_path)

    def share(self):
        pass

    def download(self):
        pass

    def play(self, song: Union[Song,Episode]):
        
        song.audio.play()

    def like(self) -> None:
        
        self.liked = not self.liked