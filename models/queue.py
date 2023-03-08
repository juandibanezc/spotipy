from .song import Song
from .episode import Episode
from typing import Union

class Queue:

    def __init__(self, songs: Union[Song,Episode]):
        self.songs = songs

    def play(self):
        pass
    
    def back(self):
        pass
    
    def next(self):
        pass
    
    def add(self):
        pass

    def drop(self):
        pass

    def change_order(self):
        pass