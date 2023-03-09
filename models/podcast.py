from .files import JPEGFile

class Podcast:
    def __init__(self, description: str, name: str, duration_ms: int, image_file_path: str, episodes: list, publisher: str):
        self.description = description
        self.name = name
        self.duration_ms = duration_ms
        self.image = JPEGFile(image_file_path)
        self.episodes = episodes
        self.publisher = publisher
        
    
    def __repr__(self) -> str:
        return 'Podcast'

    def show(self):
        print('*** Podcast ***')
        print('* Name:', self.name)
        print('* Description:', self.description)
        print('* Total duration:', self.duration_ms)
        print('* Publisher:', self.publisher)
        print('* Episodes:')
        j = 1
        for i in self.episodes:
            print(f'{j}. {i.name}')
            j = j+1

    def follow(self):
        pass

    def share(self):
        pass

    def see_all_episodes(self):
        pass