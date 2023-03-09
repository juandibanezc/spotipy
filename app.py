from models.song import Song
from models.episode import Episode
from models.album import Album
from models.podcast import Podcast
from models.artist import Artist
from random import shuffle
from interactive_functions import *
import json

f_1 = open('inputs/album_1.json')
f_2 = open('inputs/album_2.json')
a_1 = open('inputs/artist_1.json')
a_2 = open('inputs/artist_2.json')
p_1 = open('inputs/podcast_1.json')
p_2 = open('inputs/podcast_2.json')

bb_album = dict(json.load(f_1))
morat_album = dict(json.load(f_2))
bb_artist = dict(json.load(a_1))
morat_artist = dict(json.load(a_2))
podcast_1 = dict(json.load(p_1))
podcast_2 = dict(json.load(p_2))

f_1.close()
f_2.close()
a_1.close()
a_2.close()
p_1.close()
p_2.close()

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

   
  #instantiating all objects:
  top_songs_1 = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in bb_artist['top_songs']]
  top_songs_2 = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in morat_artist['top_songs']]
  
  first_list = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in bb_album['songs']]
  first_album = Album(name = bb_album['name'], duration_ms=bb_album['duration_ms'], songs=first_list)

  second_list = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in morat_album['songs']]
  second_album = Album(name = morat_album['name'], duration_ms=morat_album['duration_ms'], songs=second_list)
  
  albums_selections = {
     '1':first_album,
     '2':second_album
  }
  
  # Generating Artist objects
  first_artist = Artist(name = bb_artist['name'], popularity=bb_artist['popularity'], 
                        followers=bb_artist['followers'], albums=first_album, top_songs=top_songs_1)
  
  second_artist = Artist(name = morat_artist['name'], popularity=morat_artist['popularity'], 
                        followers=morat_artist['followers'], albums=second_album, top_songs=top_songs_2)
  
  artist_selections = {
     '1':first_artist,
     '2':second_artist
  }
  
    # Second, make a list of episodes:
  first_list = [Episode(i['name'], i['duration_ms'], i['description'], i['image_file_path'], i['audio_file_path']) for i in podcast_1['episodes']]
  first_podcast = Podcast(podcast_1['description'], podcast_1['name'], podcast_1['duration_ms'], podcast_1['image_file_path'], first_list, podcast_1['publisher'])

  second_list = [Episode(i['name'], i['duration_ms'], i['description'], i['image_file_path'], i['audio_file_path']) for i in podcast_2['episodes']]
  second_podcast = Podcast(podcast_2['description'], podcast_2['name'], podcast_2['duration_ms'], podcast_2['image_file_path'], second_list, podcast_2['publisher'])


  podcast_selections = {
     '1':first_podcast,
     '2':second_podcast
  }
  
  MULTI_SELECTION = {
    '1':artist_selections,
    '2':albums_selections,
    '5':podcast_selections
  }
  
  loop_ = True
  while loop_:
    choice = library()
    
    
    if choice != '6':
      selection = MULTI_SELECTION[choice]
      selection_choice = multi_selection(selection)
      if selection_choice == '3':
        continue
      else:
        ### Aquí debe incluirse todo el tema de .show que
        ### sería el mismo método para todos, sea artist, podcast y album
        pass
      
    else:
      loop_ = False
    

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