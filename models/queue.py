from .song import Song
from .episode import Episode
from typing import Union, List

class Queue:

    def __init__(self, audio_objects: List[Union[Song,Episode]]):
        self.audio_objects = audio_objects

    def play(self):
        return self.audio_objects[0].play()

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