from models.user import User
from models.queue import Queue
from interactive_functions import *
from models.exceptions import InvalidSelectionError
from objects_instances import run_instances

def run_app():
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
    print("\nSign in to your user account\n")
    email = input("Email: ")
    password = input("Password: ")
    ## User Information
    user_1 = User(email=email, password=password)
    
    MULTI_SELECTION = run_instances()
    
    while True:
        # We call library to select options
        choice = library()
        
        # Now, seven is for exit
        
        if choice != '7':
            # Key Error Validation
            try:
                selection = MULTI_SELECTION[choice]
            
            except KeyError:
                raise InvalidSelectionError("Invalid selection. Available options are: 1,2,3,4,5,6")
            
            if choice in ['3', '5']:
                if len(selection.audio_object.audio_objects) == 0:
                    print(f'You dont have any {selection} here, please add one')
                    continue
                else:
                    selection.show()
            
            else:
                selection_choice = multi_selection(selection)
                selection[selection_choice].show()
        
            try:
                selected_song = int(input("\nSelect a song or episode to play\n"))
                selected_song -= 1

                if choice == '6':
                    user_1.queue = Queue(selection[selection_choice].episodes)
                
                elif choice in ['3', '4', '5']:
                    user_1.queue = selection[selection_choice].audio_object
                else:
                    user_1.queue = Queue(selection[selection_choice].songs)
                    
                play_name, play_action_bool = user_1.queue.play(selected_song)
                
                while True:
                    try:
                        next_command = play_action(playing=play_action_bool, 
                                                   name = play_name)
                        
                        if next_command == '0':
                            user_1.queue.shuffle()
                        elif next_command == '1':
                            user_1.queue.back()
                            play_name, play_action_bool = user_1.queue.play()
                        elif next_command == '2':
                            play_name, play_action_bool = user_1.queue.play()
                            
                        elif next_command == '3':
                            user_1.queue.next()
                            play_name, play_action_bool = user_1.queue.play()
                            
                        elif next_command == '4':
                            multimedia_liked = user_1.queue.audio_objects[user_1.queue.i]
                            user_1.give_likes(song_or_episode=multimedia_liked)
                            
                            if str(multimedia_liked) == 'Song':
                                MULTI_SELECTION['3'].add_multimedia(multimedia_liked)
                            else:
                                MULTI_SELECTION['5'].add_multimedia(multimedia_liked)
                        elif next_command == '5':
                            trick = other_options()
                            
                            if trick == '4':
                                break
                            else:
                                if trick == '1':
                                    user_1.queue.show()
                                else:
                                    continue
                        
                    except KeyboardInterrupt:
                        break
                    
            except KeyboardInterrupt:
                continue
            
        else:
            break
            
if __name__ == '__main__':
    run_app()
            
            
                
                

    
    

    
    