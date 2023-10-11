from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        all_artists = self._connection.execute("SELECT name FROM artists")
        all_artist_names = []
        for artist in all_artists:
            all_artist_names.append(artist['name'])
        return ', '.join(all_artist_names)
    
    def add(self, artist):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)", [artist.name, artist.genre])