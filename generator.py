import os
import time
from exsultate import *
from docx import Document

class Generator:
    def __init__(self):
        self.configuration = None
        self.filename = None
        self.document = None

    def load_configuration(self, filename="config.json"):
        if not os.path.isfile(filename):
            self.generate_config_file(filename)
        self.configuration = read_json(filename)
        
    @staticmethod
    def get_default_config():
        return {"style_mappings": {"verse": "verse", "chorus": "chorus", "title": "title"},
                "template": "template.docx"}

    def generate_config_file(self, filename):
        write_json(Generator.get_default_config(), filename)

    def generate(self, songbook):
        self.filename = str(time.time_ns()) + ".docx"
        self.document = Document(self.configuration['template'])

        for song in songbook.songs:
            self.add_song_to_document(song)

        self.document.save(self.filename)

    def add_song_to_document(self, song):
        self.document.add_paragraph(song.title, style=self.configuration['style_mappings']['title'])
        songparts = song.content
        for songpart in songparts:
            self.add_songpart_to_document(songpart)

    def add_songpart_to_document(self, songpart):
        self.document.add_paragraph(songpart.lyrics(), style=self.configuration['style_mappings'][songpart.type])