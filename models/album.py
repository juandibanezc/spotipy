from .spotipy import Spotipy
from .song import Song
from .queue import Queue
from typing import List
from .artist import Artist

class Album(Spotipy):

    def __init__(self, name: str, duration_ms: int = None, file_path: str = '.jpeg', 
                 release_year: str = None, songs: List[Song] = ['',''], album_type: str = None, artist: Artist = None):
        super().__init__(name, duration_ms, file_path)
        self.artist = artist
        self.release_year = release_year
        self.songs = songs
        self.total_songs = len(songs)
        self.album_type = album_type
        
    def __repr__(self) -> str:
        return 'Album'

    def play(self):
        
        album_queue = Queue(self.songs)

        return album_queue.play()
    
    def show(self):
        j = 1
        for i in self.songs:
            print(f'{j}. {i.name}')
            j = j+1
    
    def share(self):
        return super().share()
    
    def download(self):
        return super().download()
    
    def like(self):
        return super().like()