#!/usr/bin/python

import csv, json, os, requests, sys

from datetime import date
from pathlib import Path
#from pprint import pformat, pprint

from tools import clean_label

USAGE_INFO = """usage: python index.py <filename.csv>
"""#; print(sys.argv)

SCRIPT_PATH = os.getcwd() + '/'#; print(SCRIPT_PATH)
DATA_PATH = SCRIPT_PATH + 'data/'
if not Path(DATA_PATH).is_dir():
    os.mkdir(DATA_PATH)

if len(sys.argv) < 2:
    print(USAGE_INFO)
    sys.exit("ERROR: mandatory parameter (sources file) is missing")
else:
    SOURCE_PATH = SCRIPT_PATH + sys.argv[1]
    SOURCE_FILE = Path(SOURCE_PATH)
    if not SOURCE_FILE.is_file():
        print(USAGE_INFO)#; print(SOURCE_PATH, SOURCE_FILE)
        sys.exit("ERROR: source file doesn't seem to exist")

if __name__ == '__main__':
    os.system('clear')
    with open(SOURCE_FILE, 'r') as source_file:
        for line in source_file:
            source = line.split(',')
            source_label = source[0]
            source_address = source[1].strip()
            if len(source) >= 3:
                source_type = source[2]
            elif 'csv' in source[1]:
                source_type = 'csv'
            elif 'json' in source[1]:
                source_type = 'json'
            else:
                source_type = '???'
            print(f"Parsing {source_type} source '{source_label}'..",
                end = ' ',
                flush = True
            )
            response = requests.get(source_address)
            if response.status_code == 200:
                file_type = 't'
                if source_type == 'csv':
                    data = list(csv.reader(response.text))
                    dump = response.text
                elif source_type == 'json':
                    data = json.loads(response.text)
                    dump = response.text
                else: # autodetecting source type..
                    if 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in response.headers['Content-Type']:
                        source_type = 'xlsx'
                        data = None # TBD https://www.marsja.se/your-guide-to-reading-excel-xlsx-files-in-python/
                        dump = response.content
                        file_type = 'b'
                with open(DATA_PATH + date.today().strftime('%Y-%m-%d') + '_' + clean_label(source_label) + '.' + source_type, 'w' + file_type) as data_file:
                    data_file.write(dump)
                print("OK!")
            else:
                print("Error: " + response.status_code)
