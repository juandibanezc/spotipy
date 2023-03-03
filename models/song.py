from spotipy import Spotipy
from multimedia import Multimedia


class Song(Spotipy, Multimedia):
    
    def __init__(self, name, duration_ms, image, liked, playing, lyrics, reproductions):
        super().__init__(name, duration_ms, image)
        self.liked = liked
        self.playing = playing
        self.reproductions = reproductions
        self.lyrics = lyrics

    def shuffle(self):
        pass

    def repeat(self):
        pass

    def see_artist(self):
        pass

    def go_to_radio(self):
        pass

    # from Spotipy class

    def share(self):
        return super().share()
    
    def download(self):
        return super().download()
    
    def play(self):
        return super().play()
    
    def like(self):
        return super().like()
    
    # From multimedia class

    def next(self):
        return super().next()
    
    def back(self):
        return super().back()
    
    def add_to_playlist(self):
        return super().add_to_playlist()
    
    def add_to_queue(self):
        return super().add_to_queue()