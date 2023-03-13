from .spotipy import Spotipy
from .multimedia import Multimedia


class Episode(Spotipy, Multimedia):

    def __init__(self, name:str, duration_ms: int, description:str, image_file_path:str,
                      audio_file_path:str, liked: bool = False, playing: bool = False):
        Spotipy.__init__(self, name = name, duration_ms = duration_ms, file_path = image_file_path)
        Multimedia.__init__(self, liked = liked, playing = playing, file_path = audio_file_path)
        self.description = description

    # Defined self methods of the class Episode

    def show(self):
        print('*** Episode ***\n')
        print('\n* Name:', self.name)
        print('\n* Duration:', self._Spotipy__duration_ms)
        print('\n* Description:', self.description)

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
        return self.audio.play()
    
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