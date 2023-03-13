from queue import Queue

class User:

    def __init__(self, email: str, password: str,  name: str = None, 
                 premium: bool = False, queue: Queue = None) -> None:
        
        self.name = name
        self.email = email
        self.password = password
        self.premium = premium
        self.queue = queue

    def give_likes(self, song_or_episode):
        song_or_episode.liked == True
        return True