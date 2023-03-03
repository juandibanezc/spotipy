from spotipy import Spotipy

class Album(Spotipy):

    def __init__(self, name, duration_ms, image, release_year, songs, total_songs, album_type):
        super().__init__(name, duration_ms, image)

        self.release_year = release_year
        self.songs = songs
        self.total_songs = total_songs
        self.album_type = album_type

    def play(self):
        return super().play()
    
    def share(self):
        return super().share()
    
    def download(self):
        return super().download()
    
    def like(self):
        return super().like()