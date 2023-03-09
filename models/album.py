from .spotipy import Spotipy
from .song import Song
from .queue import Queue
from typing import List

class Album(Spotipy):

    def __init__(self, name: str, duration_ms: int = None, file_path: str = '.jpeg', 
                 release_year: str = None, songs: List[Song] = None, album_type: str = None):
        super().__init__(name, duration_ms, file_path)

        self.release_year = release_year
        self.songs = songs
        self.total_songs = len(songs)
        self.album_type = album_type

    def play(self):
        
        album_queue = Queue(self.songs)

        return album_queue.play()
    
    def show_album(self):
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