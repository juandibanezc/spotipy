from .files import MP3File

class Multimedia:
    def __init__(self, liked: bool, playing: bool, file_path: str):
        self.liked = liked
        self.playing = playing
        self.audio = MP3File(file_path)

    def next(self):
        pass

    def back(self):
        pass

    def add_to_playlist(self):
        pass

    def add_to_queue(self):
        pass