from models.song import Song
import json
from models.album import Album
from random import shuffle

f_1 = open('inputs/album_1.json')
f_2 = open('inputs/album_2.json')

bb_album = dict(json.load(f_1))
morat_album = dict(json.load(f_2))

f_1.close()
f_2.close()

def run_app(play = False):

  print("""
  
  ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⡿⠿⠛⠛⠛⠉⠉⠉⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣇⠀⣀⣀⣠⣤⣤⣤⣤⣠⣀⣀⠀⠀⠀⠈⠙⠻⣿⣿⣷⠀
⢠⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠘⠺⠿⢿⣿⣶⣤⣀⣠⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣇⣀⣀⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠉⠛⢿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠛⠿⠿⣿⣶⣦⣤⣾⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣤⣤⣤⣤⣶⣶⣦⣤⣤⣄⡀⠈⠙⣿⣿⣿⣿⣿⡿⠀
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
  
  
  """)
  print('')
  print('Welcome to Spotify')

  # First, make a list of songs:
  first_list = [Song(i['name'], i['duration_ms']) for i in bb_album['songs']]
  first_album = Album(name = bb_album['name'], duration_ms=bb_album['duration_ms'], songs=first_list)

  second_list = [Song(i['name'], i['duration_ms']) for i in morat_album['songs']]
  second_album = Album(name = morat_album['name'], duration_ms=morat_album['duration_ms'], songs=second_list)


  albums_selections = {
     '1':first_album,
     '2':second_album
  }

  print('''
  Library:
  
  1. Albums
  2. Your Episodes
  3. Playlist

  ''')

  print(f'''

  You have two albums in Your Library:

  1. {first_album.name}
  2. {second_album.name}
  
  Select one album

  ''')

  key = input('> ')
  albums_selection = albums_selections[key]
  print(f'These are the songs of {albums_selection.name}')
  albums_selection.show()
  

  if play:
    songDict = {
        "name": "Flowers",
        "audio_file_path": "files/audios/Forever_Young_Otis_McDonald.mp3",
        "duration_ms": "242",
        "image_file_path": "files/images/otis_mcdonald.jpeg",
    }

    song1 = Song(name="Flowers", audio_file_path="files/audios/Forever_Young_Otis_McDonald.mp3",
                duration_ms=123, image_file_path="files/images/otis_mcdonald.jpeg"
                )

    song1.play()

if __name__ == '__main__':
    run_app()