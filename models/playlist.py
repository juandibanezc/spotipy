from .spotipy import Spotipy
from .queue import Queue

class Playlist(Spotipy):

    def __init__(self, name:str = '', image_file_path:str = 'jpeg', public: bool = False, 
                 collaborative: bool = False, collaborators: list = [], creator: str = None, likes: int = None, 
                 audio_objects:list = [], description:str = ''):
        
        if audio_objects == None:
            duration_ms = 0
        else: 
            duration_ms = sum([song._Spotipy__duration_ms for song in audio_objects])
        
        super().__init__(name = name, duration_ms = duration_ms, file_path = image_file_path)

        self.public = public
        self.collaborative = collaborative
        self.collaborators = collaborators
        self.creator = creator
        self.likes = likes
        self.audio_object = Queue(audio_objects)
        self.total_songs = len(audio_objects)
        self.description = description
        
    def __repr__(self) -> str:
        return 'Playlist'
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

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
        for i, song in enumerate(self.audio_object.audio_objects):
            print(f'** {i+1}. {song.name}')

    def add_multimedia(self, sound_object):
        if self.name == 'Liked Songs' or self.name == 'Your Episodes':
            if sound_object.liked and sound_object not in self.audio_object.audio_objects:
                self.audio_object.audio_objects.append(sound_object)
                self.total_songs = len(self.audio_object.audio_objects)
                self._Spotipy__duration_ms = sum([song._Spotipy__duration_ms for song in self.audio_object.audio_objects])
            else:
                self.audio_object.audio_objects.remove(sound_object)
        else:
            self.audio_object.audio_objects.append(sound_object)
            self.total_songs = len(self.audio_object.audio_objects)
            self._Spotipy__duration_ms = sum([song._Spotipy__duration_ms for song in self.audio_object.audio_objects])
        

    def remove_song(self, sound_object):
        print(f'You sure that you want to remove {self.audio_object.audio_objects[sound_object].name} from your playlist?')
        choice = int(input("(1.Y / 2.N)>"))
        if choice == 1:
            self.audio_object.audio_objects.remove(sound_object)
        else:
            pass
        

    def add_collaborators(self):
        pass

    def remove_collaborators(self):
        pass
 
    def play(self, object_selected = None):
        return self.audio_object.play(song_selected = object_selected)
    
    # Methods from Spotipy class
    
    def download(self):
        return super().download()
    
    def share(self):
        return super().share()
