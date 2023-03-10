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
        5. Your Episodes (Podcast)
        6. Exit
  
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
        
        print(f'''

          You have selected the {class_object} Liked Songs:
          
          Thinking what to do :v
          
          3. Back to the Library menu

          ''')
      
      return input('>')