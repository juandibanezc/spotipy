from .files import JPEGFile

class Spotipy:
    def __init__(self, name: str, duration_ms: int, file_path: str):
        self.name = name
        self.__duration_ms = duration_ms
        self.image = JPEGFile(file_path)

    def share(self):
        pass

    def download(self):
        pass

    def like(self) -> None:
        
        self.liked = not self.liked