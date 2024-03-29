from .spotipy import Spotipy
from .song import Song
from .queue import Queue
from typing import List
from .artist import Artist

class Album(Spotipy):

    def __init__(self, name: str, duration_ms: int = None, file_path: str = '.jpeg', author: str = None, 
                 release_date: str = None, songs: List[Song] = ['',''], album_type: str = None):
        super().__init__(name, duration_ms, file_path)
        self.author = author
        self.release_date = release_date
        self.songs = songs
        self.total_songs = len(songs)
        self.album_type = album_type
        
    def __repr__(self) -> str:
        return 'Album'

    def play(self, selected_song = None):
        
        album_queue = Queue(self.songs)

        return album_queue.play(selected_song = selected_song)
    
    def show(self):
        print('*** Album ***')
        print('\n* Name:', self.name)
        print(f'\n* Total duration: {self._Spotipy__duration_ms} ms')
        print('\n* Author:', self.author)
        print('\n* Release date:', self.release_date)
        print('\n* Total songs:', self.total_songs)
        print('\n* Album type:', self.album_type)
        print('\n* Songs:')
        for i, song in enumerate(self.songs):
            print(f'** {i+1}. {song.name}')
    
    # Methods from Spotipy class
    
    def share(self):
        return super().share()
    
    def download(self):
        return super().download()