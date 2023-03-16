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
            try:
                return self.audio_objects[self.i].name, self.audio_objects[self.i].play()
            except IndexError:
                self.i = 0
                return self.audio_objects[self.i].name, self.audio_objects[self.i].play()
        else:
            self.i = song_selected
            try:
                return self.audio_objects[song_selected].name, self.audio_objects[song_selected].play()
            except IndexError:
                self.i = 0
                song_selected = 0
                return self.audio_objects[song_selected].name, self.audio_objects[song_selected].play()

    def back(self):
        self.i -= 1
    
    def next(self):
        self.i += 1
    
    def add(self, new_audio_object:Union[Song, Episode]):
        self.audio_objects.append(new_audio_object)
        print(f"You added {new_audio_object.name} to your Queue")

    def drop(self, song_selected):
        print(f'You sure that you want to remove {self.audio_objects[song_selected].name} from your Queue?')
        choice = int(input("(1.Y / 2.N)>"))
        if choice == 1:
            self.audio_objects.pop(song_selected)
        else:
            pass

    def change_order(self, audio_1, audio_2):
        self.audio_objects[audio_1], self.audio_objects[audio_2] = self.audio_objects[audio_2], self.audio_objects[audio_1]
        print("Order changed!!")
    
    def show(self):
        print('\n* Songs or Episodes in Queue:')
        for j, song in enumerate(self.audio_objects[self.i+1:]):
            print(f'** {j+1}. {song.name}')
    
    def shuffle(self):
        random.shuffle(self.audio_objects)
        print("You shuffle your Queue")