from generator import Generator
from song import SongBook
from exsultate import *
import json
import sys
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    log_filename = os.path.dirname(os.path.realpath(__file__)) + '/log.txt'
    os.system("echo 'beginning' >> " + log_filename)
    json_string = sys.argv[1]
    filename = ''
    if(len(sys.argv) > 2 ):
        filename = sys.argv[2]
    os.system("echo 'captured command line arguments' >> " + log_filename)
    generator = Generator()
    generator.load_configuration()
    os.system("echo 'loaded configuration' >> " + log_filename)
    os.system("echo 'json:' >> " + log_filename)
    os.system("echo " + json_string + " >> " + log_filename)
    dictionary = json.loads(json_string)
    os.system("echo 'read dictionary from json' >> " + log_filename)
    songbook = SongBook.from_dict(dictionary)
    # songbook = SongBook.from_dict(read_json( dir_path + '/' + 'songbook2.json'))
    os.system("echo 'about to generate shit' >> " + log_filename)
    output = generator.generate(songbook, filename)
    os.system("echo 'generated shit' >> " + log_filename)
    print(output)

if __name__ == '__main__':
    main()