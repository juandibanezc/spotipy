from .files import JPEGFile
from .spotipy import Spotipy

class Podcast(Spotipy):
    def __init__(self, description: str, name: str, duration_ms: int, image_file_path: str, episodes: list, publisher: str):
        self.description = description
        self.episodes = episodes
        self.publisher = publisher
        super().__init__(name = name, duration_ms = duration_ms, file_path = image_file_path)
        
    
    def __repr__(self) -> str:
        return 'Podcast'

    def show(self):
        print('*** Podcast ***\n')
        print('\n* Name:', self.name)
        print('\n* Description:', self.description)
        print('\n* Total duration:', self.__duration_ms)
        print('\n* Publisher:', self.publisher)
        print('\n* Episodes:')
        for i, episode in enumerate(self.episodes):
            print(f'** {i+1}. {episode.name}')

    def follow(self):
        pass

    # Methods from Spotipy class
    
    def download(self):
        return super().download()
    
    def share(self):
        return super().share()