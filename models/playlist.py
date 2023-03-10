from .spotipy import Spotipy

class Playlist(Spotipy):

    def __init__(self, name:str = '', duration_ms:int = 0, image:str = 'jpeg', public: bool = False, 
                 collaborative: bool = False, collaborators:int = 0, creator: str = None, likes: int = None, 
                  songs = None, description:str = ''):
        super().__init__(name, duration_ms, image)

        self.public = public
        self.collaborative = collaborative
        self.collaborators = collaborators
        self.creator = creator
        self.likes = likes
        self.songs = songs
        self.total_songs = len(songs)
        self.description = description
        
    def __repr__(self) -> str:
        return 'Playlisr'

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
