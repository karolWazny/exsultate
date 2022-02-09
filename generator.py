import os
from exsultate import *

class Generator:
    def __init__(self):
        self.configuration = None

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