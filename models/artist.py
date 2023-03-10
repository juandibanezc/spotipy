from typing import List


class Artist:

    def __init__(self, name:str, popularity:int, followers:int, albums: list, top_songs: list):
        self.name = name
        self.popularity = popularity
        self.followers = followers
        self.albums = albums
        self.top_songs = top_songs
        
    
    def __repr__(self) -> str:
        return 'Artist'
    
    def play(self):
        pass
    
    def show(self):
        print('*** Artist ***\n')
        print('\n* Name:', self.name)
        print('\n* Popularity:', self.popularity)
        print('\n* Followers:', self.followers)
        print('\n* Albums:')
        for i, album in enumerate(self.albums):
            print(f'** {i+1}. {album.name}')
        print('\n* Top songs:')
        for i, song in enumerate(self.top_songs):
            print(f'** {i+1}. {song.name}')
            
            
    def share(self):
        pass

    def block(self):
        pass

    def follow(self):
        pass

    def go_to_radio(self):
        pass