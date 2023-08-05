"""Demonstrates return values in functions"""


def make_album(artist, album, song_number=None):
    """This function takes the names of an artist, album and song number(optional)
      and returns a dictionary"""
    if song_number:
        new_album = {
            'artist': artist,
            'album': album,
            'song_number': song_number
            }
    else:
        new_album = {
            'artist': artist,
            'album': album,
            }

    return new_album
    

kendrick = make_album('Kendick', 'Damn')
print(kendrick)

drake = make_album('Drake', 'Views', 20 )
print(drake)


# Functions can be used within loops
while True:
    print(f'\nPlease input an artist and on of thier albums\n')
    print(f'To quit press "q" twice and enter')

    artist = input('Artist name:\n')
    if artist == 'qq':
        break

    album = input('Album name:\n')
    if album == 'qq':
        break

    new_album = make_album(artist, album)
    print(new_album)
