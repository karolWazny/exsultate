class Song:
    def __init__(self, title):
        self.title = title
        self.lyrics_author = None
        self.music_author = None
        self.translation_author = None
        self.content = []

    def add_song_part(self, songpart):
        self.content.append(songpart)

class SongPart:
    def __init__(self, content, type='verse'):
        self.content = content
        self.type = type