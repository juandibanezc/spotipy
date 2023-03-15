from .spotipy import Spotipy

class Playlist(Spotipy):

    def __init__(self, name:str = '', image_file_path:str = 'jpeg', public: bool = False, 
                 collaborative: bool = False, collaborators: list = [], creator: str = None, likes: int = None, 
                  songs: list = None, description:str = ''):
        super().__init__(name, sum([song._Spotipy__duration_ms for song in songs]), image_file_path)

        self.public = public
        self.collaborative = collaborative
        self.collaborators = collaborators
        self.creator = creator
        self.likes = likes
        self.songs = songs
        self.total_songs = len(songs)
        self.description = description
        
    def __repr__(self) -> str:
        return 'Playlist'

    def show(self):
        print('*** Playlist ***\n')
        print('\n* Name:', self.name)
        print('\n* Description:', self.description)
        print('\n* Total duration:', self._Spotipy__duration_ms)
        print('\n* Creator:', self.creator)
        print('\n* Public:', self.public)
        print('\n* Collaborative:', self.collaborative)
        print('\n* Likes:', self.likes)
        print('\n* Total songs:', self.total_songs)
        print('\n* Songs:')
        for i, song in enumerate(self.songs):
            print(f'** {i+1}. {song.name}')

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
