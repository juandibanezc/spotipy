from models.song import Song
from models.episode import Episode
from models.album import Album
from models.podcast import Podcast
from models.artist import Artist
from models.playlist import Playlist
from models.user import User
from models.queue import Queue
import random
from interactive_functions import *
from models.exceptions import InvalidSelectionError
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
  print('\nWelcome to Spotify')

   
  #instantiating all objects:

  # User
  print("\nSign in to your user account\n")
  email = input("Email: ")
  password = input("Password: ")
  user_1 = User(email=email, password=password)

  # Albums and songs
  top_songs_1 = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in bb_artist['top_songs']]
  top_songs_2 = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in morat_artist['top_songs']]
  
  first_list = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in bb_album['songs']]
  first_album = Album(name = bb_album['name'], duration_ms=bb_album['duration_ms'], songs=first_list, author=bb_album['author'], release_date=bb_album['release_date'], album_type=bb_album['album_type'], file_path=bb_album["images"][-1]["url"])

  second_list = [Song(i['name'], i['duration_ms'], artist=i['artist']) for i in morat_album['songs']]
  second_album = Album(name = morat_album['name'], duration_ms=morat_album['duration_ms'], songs=second_list, author=morat_album['author'], release_date=morat_album['release_date'], album_type=morat_album['album_type'], file_path=morat_album["images"][-1]["url"])
  
  all_songs = first_list+second_list
  random.shuffle(all_songs)

  albums_selections = {
     '1':first_album,
     '2':second_album
  }
  
  # Artists
  first_artist = Artist(name = bb_artist['name'], popularity=bb_artist['popularity'], 
                        followers=bb_artist['followers'], albums=[first_album], top_songs=top_songs_1)
  
  second_artist = Artist(name = morat_artist['name'], popularity=morat_artist['popularity'], 
                        followers=morat_artist['followers'], albums=[second_album], top_songs=top_songs_2)
  
  artist_selections = {
     '1':first_artist,
     '2':second_artist
  }
  
  
  # Podcasts and episodes
  first_list = [Episode(i['name'], i['duration_ms'], i['description'], i['image_file_path'], i['audio_file_path']) for i in podcast_1['episodes']]
  first_podcast = Podcast(podcast_1['description'], podcast_1['name'], podcast_1['duration_ms'], podcast_1['image_file_path'], first_list, podcast_1['publisher'])

  second_list = [Episode(i['name'], i['duration_ms'], i['description'], i['image_file_path'], i['audio_file_path']) for i in podcast_2['episodes']]
  second_podcast = Podcast(podcast_2['description'], podcast_2['name'], podcast_2['duration_ms'], podcast_2['image_file_path'], second_list, podcast_2['publisher'])


  podcast_selections = {
     '1':first_podcast,
     '2':second_podcast
  }


  # Playlists
  liked_songs = Playlist(name = 'Liked Songs', songs = random.choices(all_songs, k=2))
  first_playlist = Playlist(name = 'Party all night', songs = random.choices(all_songs, k=10),creator= "Juan", likes=1, description="Perfect playlist to dance all night and party like there's no tomorrow.")
  second_playlist = Playlist(name = 'Study time', songs = random.choices(all_songs, k=10), creator= "Fernando", likes=1, description="Songs that will help to concentrate and study more smoothly.")

  playlist_selections = {
     '1':first_playlist,
     '2':second_playlist
  }
  
  MULTI_SELECTION = {
    '1':artist_selections,
    '2':albums_selections,
    '3':liked_songs,
    '4':playlist_selections,
    '5':podcast_selections
  }
  
  while True:
    choice = library()
    
    
    if choice != '6':
      try:
        selection = MULTI_SELECTION[choice]
        
      except KeyError:
        
        raise InvalidSelectionError("Invalid selection. Available options are: 1,2,3,4,5,6")
      
        
      selection_choice = multi_selection(selection)
      
      selection[selection_choice].show()

      try:
        selection_choice = input("\nSelect a song or episode to play\n")

        if choice == "5":
          user_1.queue = Queue(selection[selection_choice].episodes)
          
        else:
          user_1.queue = Queue(selection[selection_choice].songs)
          
        while True:
          
          try:
            user_1.queue.play()
            
            next_command = input("Next command?") # improve in interactive functions?
            
            user_1.queue.next()
            
          except KeyboardInterrupt:
            break

      except KeyboardInterrupt:
        continue

    else:
      break

if __name__ == '__main__':
    run_app()