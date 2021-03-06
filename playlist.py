# create play list application using nested  dictionary /list combination
def song(song_name: str, artist: str, year: int):
    return {
        'song-name': song_name,
        'artist': artist,
        'year': year
    }


playlist = {
    'bhargav': [
        song('Dynamite', 'BTS', 2020),
        song('Closer', 'Halsey', 2016),
        song('Playdate', 'ABC', 2019)
    ],
    'yash': [
        song('Song A', 'Artist A', 2016),
        song('Song B', 'Artist B', 2018),
        song('Song C', 'Artist C', 2016)
    ]
}

print(playlist['bhargav'][1])
