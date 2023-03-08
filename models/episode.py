from spotipy import Spotipy
from multimedia import Multimedia


class Episode(Spotipy, Multimedia):

    def __init__(self, name, duration_ms, liked, playing, description, transcript, audio, file_path):
        Spotipy.__init__(self, name, duration_ms, file_path)
        Multimedia.__init__(self, liked, playing, file_path)
        self.description = description
        self.transcript = transcript
        self.audio = audio

    # Defined self methods of the class Episode

    def next_episode(self):
        pass

    def add_to_users_episodes(self):
        pass

    # Defined first heritance methods Spotipy

    def share(self):
        return super().share()
    
    def download(self):
        return super().download()
    
    def play(self):
        return super().play()
    
    def like(self):
        return super().like()
    
    # Defined second heritance methods Multimedia

    def next(self):
        return super().next()
    
    def back(self):
        return super().back()
    
    def add_to_playlist(self):
        return super().add_to_playlist()
    
    def add_to_queue(self):
        return super().add_to_queue()