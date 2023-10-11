# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
"""
When I call POST /albums with album info
That album is now in the list in GET /albums
"""

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post("/albums", data = {'title': 'Scarlet',
        'release_year': '2023',
        'artist_id': '3'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""\

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Scarlet, 2023, 3)"
    
def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post("/albums")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == ""\
    "You need to submit a title, release year and artist id"

# POST /albums
    # title: 'Doolittle'
    # release_year: 1989
    # artist_id: 1
# Expected response (200 OK)
"(No content)"

# Get /albums
# Expected resoinse (200 OK)
""""
Album(1, 'Doolittle', 1989, 1)
Album(2, 'Surfer Rosa', 1988, 1)
"""

# POST /albums
# Expected response (400 Bad Request)

"You need to submit a title, release_year, and artist_id"

##################

"""# Request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone"""

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"


"""# Request:
POST /artists
# With body parameters:
name=Wild nothing
genre=Indie
# Expected response (200 OK)
(No content)"""

def test_post_artists(web_client):
    response = web_client.post('/artists', data = {'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

# """# Then subsequent request:
# GET /artists
# # Expected response (200 OK)
# Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"""

def test_get_artists_added_one(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"