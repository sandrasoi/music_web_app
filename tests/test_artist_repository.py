from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""artist repository:
Given a list of artists
Show me all the artists names

repository.all() => Pixies, Abba"""

def test_list_all_artists(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == "Pixies, ABBA"

# """Given an artist is added to a list
# Show me the updated list of artist names with the added artist"""

def test_list_all_artists(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Doja Cat", "Pop")
    repository.add(artist)
    repository.all() == "Pixies, Abba, Doja Cat, Taylor Swift, Nina Simone"

