

class User:

    def __init__(self, email: str, password: str,  name: str = None, 
                 premium: bool = False, queue = None) -> None:
        
        self.name = name
        self.email = email
        self.password = password
        self.premium = premium
        self.queue = queue

    def give_likes(self, song_or_episode):
        song_or_episode.liked = not song_or_episode.liked
        
        if str(song_or_episode) == 'Song':
            if song_or_episode.liked:
                print(f"Now {song_or_episode.name} is in your liked songs!")
            
            else:
                print(f"Now {song_or_episode.name} is not in your liked songs!")
        else:
            if song_or_episode.liked:
                print(f"Now {song_or_episode.name} is in Your Episodes!")
            
            else:
                print(f"Now {song_or_episode.name} is not in Your Episodes!") 