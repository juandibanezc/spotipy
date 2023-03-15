from .song import Song
from .episode import Episode
from typing import Union, List
import random

class Queue:

    
    def __init__(self, audio_objects: List[Union[Song,Episode]]):
        self.audio_objects = audio_objects
        self.i = 0

    def play(self, song_selected = None) -> tuple:
        if song_selected == None:
            return self.audio_objects[self.i].name, self.audio_objects[self.i].play()
        else:
            self.i = song_selected
            return self.audio_objects[song_selected].name, self.audio_objects[song_selected].play()

    def back(self):
        self.i -= 1
    
    def next(self):
        self.i += 1
    
    def add(self, new_audio_object:Union[Song, Episode]):
        self.audio_objects.append(new_audio_object)
        print(f"You added {new_audio_object.name} to your Queue")

    def drop(self, song_selected):
        pass

    def change_order(self):
        pass
    
    def shuffle(self):
        random.shuffle(self.audio_objects)
        print("You shuffle your Queue")