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
        print('*** Podcast ***\n')
        print('\n* Name:', self.name)
        print('\n* Description:', self.description)
        print('\n* Total duration:', self.duration_ms)
        print('\n* Publisher:', self.publisher)
        print('\n* Episodes:')
        for i, episode in enumerate(self.episodes):
            print(f'** {i+1}. {episode.name}')

    def follow(self):
        pass

    def share(self):
        pass

    def see_all_episodes(self):
        pass