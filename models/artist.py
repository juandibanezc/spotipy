from typing import List


class Artist:

    def __init__(self, name:str, popularity:int, followers:int, albums, top_songs):
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
        
        j = 1
        for i in self.top_songs:
            print(f'{j}. {i.name}')
            j = j+1
            
            
    def share(self):
        pass

    def block(self):
        pass

    def follow(self):
        pass

    def go_to_radio(self):
        pass