from .song import Song
from .episode import Episode
from typing import Union, List

class Queue:

    
    def __init__(self, audio_objects: List[Union[Song,Episode]]):
        self.audio_objects = audio_objects
        self.i = 0

    def play(self):
        return self.audio_objects[0].play()

    def back(self):
        '''
        Se supone debe devolverse
        '''
        self.i -= 1
        return self.audio_objects[self.i].play()
    
    def next(self):
        self.i += 1
        return self.audio_objects[self.i].play()
    
    def add(self):
        pass

    def drop(self):
        pass

    def change_order(self):
        pass
    
    def shuffle(self):
        pass