from _6_imports.albums import make_album, add_album



def test_make_album():
    """Does the fucntion work?"""
    album_with_number = make_album('Frank Ocean', 'Blond', 12) 
    assert album_with_number == {'artist': 'Frank Ocean', 'album': 'Blond',\
                                'song_number': 12}
