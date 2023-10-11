# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user 
So that I can see all the artists
Show me a list of all artists

As a user
So that I can add artists with a name and genre
I want to add an artist to the list of other artists

```python
# EXAMPLE

class Artist:
    # User-facing properties:
    #   name: string

    def __init__(self, name, genre):
        # Parameters:
        #   name: string
         #    genre: string
        # Side effects:
        #   Sets the name property of the self object
        # Sets the genre property of the self object
        pass # No code here yet

    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        #returns nicely formatted string


class ArtistRepository:
        def __init__(self):
            pass # No code here yet

        def add(self, artist):
            parameters: artist object
            returns nothing

        def all(self):
            returns list of all artists names
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

artist repository:
Given a list of artists
Show me all the artists names

repository.all() => Pixies, Abba

Given an artist is added to a list
Show me the updated list of artist names with the added artist

repository.add(Artist(Doja Cat, Pop))
repository.all() => Pixies, Abba, Doja Cat

artist model:
Given an artist has been added with name and genre
Check that the name and genre properties are correct

artist = Artist('Doja Cat', 'Pop')
artist.name = 'Doja Cat'
artist.genre = 'Pop'

Given two artist objects with the same name and genre
Return that they are the same

artist1 = Artist('Doja Cat', 'Pop')
artist2 = Artist('Doja Cat', 'Pop')
artist1 == artist2 => returns True


Return artist as a nicely formatted string
artist = Artist('Doja Cat', 'Pop') => Artist('Doja Cat', 'Pop')


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->