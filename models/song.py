from models.spotipy import Spotipy
from models.multimedia import Multimedia
from typing import List
from .artist import Artist

class Song(Spotipy, Multimedia):
    
    def __init__(self, name, duration_ms, audio_file_path = '.mp3', image_file_path = '.jpeg',
                  liked = False, playing = False, reproductions = 0, artist:List[Artist] = None):
        
        Spotipy.__init__(self, name=name, duration_ms=duration_ms, file_path=image_file_path)
        
        Multimedia.__init__(self, liked=liked, playing=playing, file_path=audio_file_path)
        self.reproductions = reproductions
        self.artist = artist
        
    def __repr__(self) -> str:
        return 'Song'
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def show(self):
        print('*** Song ***\n')
        print('\n* Name:', self.name)
        print('\n* Duration:', self._Spotipy__duration_ms)
        print('\n* Artists:')
        for i, artist in enumerate(self.artist):
            print(f'** {i+1}. {artist}')

    def repeat(self):
        pass

    def see_artist(self):
        pass

    def go_to_radio(self):
        pass
    
    def play(self):
        self.playing = not self.playing
        
        if self.playing:
            print(f"You are playing: {self.name}")

            return self.playing
        else:
            print(f"You are in Pause")

            return self.playing
        
    # from Spotipy class

    def share(self):
        return super().share()
    
    def download(self):
        return super().download()
    
    # From multimedia class
    
    def add_to_playlist(self):
        return super().add_to_playlist()
    
    def add_to_queue(self):
        return super().add_to_queue()