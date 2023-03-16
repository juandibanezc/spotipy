from models.album import Album
from models.artist import Artist
from models.podcast import Podcast
from typing import Union

def library() -> str:
  
  print('''
      Library:
        
        1. Artists
        2. Album
        3. Liked Songs  
        4. Playlists   
        5. Your Episodes
        6. Your Podcasts
        7. Exit
  
  Select One Option
  ''')
  
  choice = input('> ')
  
  return choice

def multi_selection(multi_selec:dict) -> str:
      
      ## Extract only one object of the option selected
      try:
        class_object = multi_selec['1']
        
        print(f'''

          You have two {class_object}s in Your Library:

          1. {multi_selec['1'].name}
          2. {multi_selec['2'].name}
          
          Select one {class_object} or:
          
          3. Back to the Library menu

          ''')
      except TypeError:
        
        class_object = multi_selec

        if multi_selec.songs == None:
          print(f'''

            You do not have any songs in {class_object.name}.
            
            Like a song to add to your Liked Songs
            
            3. Back to the Library menu

            ''')
      
        print(f'''

          You have selected the {class_object} Liked Songs:
          
          Thinking what to do :v
          
          3. Back to the Library menu

          ''')
      
      return input('>')

def play_action(playing:bool, name) -> str:
   if playing:
    print(f"""
                       {name}
            -------------------------------- ♡ 
            🔀 ⏮            ⏸            ⏭  🔁""")
    
    print("0. Shuffle 1. Back  2. Pause  3. Next  4.Like 5. See Other Options")

    return input(">")

   else:
    print(f"""
                       {name}
            -------------------------------- ♡ 
            🔀 ⏮            ▶            ⏭  🔁""")
    
    print("0. Shuffle 1. Back  2. Play 3. Next  4.Like  5. See Other Options")

    return input(">")
   
def other_options() -> str:
  
  print("""
        
        1. See your Queue (show)
        2. Remove a song from your Queue (drop)
        3. Change order (show and change_order)
        4. Back to library
        """)
  
  return input(">")

def user_queue(first_selection:int, second_selection:int, list_of_songs:list = [], list_queue: list = []) -> tuple:
  
  lenght = len(list_of_songs)
  
  curse = len(list_queue)

  return lenght-curse+(first_selection-1), lenght-curse+(second_selection-1)
