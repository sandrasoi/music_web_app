# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# Request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone


# Request:
POST /artists
# With body parameters:
name=Wild nothing
genre=Indie
# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

# Request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

def test_get_artists(web_client):
  response = web_client.get('/artists')
  assert response.status_code == 200
  assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"


# Request:
POST /artists
# With body parameters:
name=Wild nothing
genre=Indie
# Expected response (200 OK)
(No content)

def test_post_artists(web_client):
  response = web_client.get('/artists')
  assert response.status_code = 200
  assert response.data.decode('utf-8') == ""

# Then subsequent request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

def get_artists_added_one(web_client):
  response = web_client.get('/artists')
  assert response.status_code = 200
  assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"



<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->