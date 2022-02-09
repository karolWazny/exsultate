from generator import Generator
from song import SongBook
from exsultate import *

def main():
    generator = Generator()
    generator.load_configuration()
    songbook = SongBook.from_dict(read_json('songbook2.json'))
    generator.generate(songbook)

if __name__ == '__main__':
    main()