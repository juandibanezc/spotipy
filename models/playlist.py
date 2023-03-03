from spotipy import Spotipy

class Playlist(Spotipy):

    def __init__(self, name, duration_ms, image, public, 
                 collaborative, collaborators, creator, likes, total_songs, songs, description):
        super().__init__(name, duration_ms, image)

        self.public = public
        self.collaborative = collaborative
        self.collaborators = collaborators
        self.creator = creator
        self.likes = likes
        self.total_songs = total_songs
        self.songs = songs
        self.description = description

    def leave(self):
        pass

    def add_song(self):
        pass

    def remove_song(self):
        pass

    def add_collaborators(self):
        pass

    def remove_collaborators(self):
        pass

    # Methods from Spotipy class

    def play(self):
        return super().play()
    
    def like(self):
        return super().like()
    
    def download(self):
        return super().download()
    
    def share(self):
        return super().share()
