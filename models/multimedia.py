from .files import MP3File

class Multimedia:
    def __init__(self, liked: bool, playing: bool, file_path: str):
        self.liked = liked
        self.playing = playing
        self.audio = MP3File(file_path)

    def play(self):
        self.playing = not self.playing
        
        if self.playing:
            print(f"You are playing: {self.name}")

            return self.playing
        else:
            print(f"You are in Pause")

            return self.playing
        
    def add_to_playlist(self):
        pass

    def add_to_queue(self):
        pass