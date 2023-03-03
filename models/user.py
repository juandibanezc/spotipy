
class User:

    def __init__(self, name, user_name, email, password, premium, queue, 
                 episodes, playlists, podcasts, artists, albums) -> None:
        
        self.name = name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.premium = premium
        self.queue = queue
        self.episodes = episodes
        self.playlists = playlists
        self.podcasts = podcasts
        self.artists = artists
        self.albums = albums

    def play(self):
        pass

    def share(self):
        pass

    def download(self):
        pass

    def like(self):
        pass