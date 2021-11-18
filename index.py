#!/usr/bin/python

USAGE_INFO = """usage: main <filename.csv>
"""

import os, sys

from pathlib import Path

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__)) + '/'

if len(sys.argv) < 2:
    print(USAGE_INFO)
    sys.exit("ERROR: mandatory parameter (sources file) is missing")
else:
    SOURCE_PATH = SCRIPT_PATH + sys.argv[1]
    SOURCE_FILE = Path(SOURCE_PATH)
    if not SOURCE_FILE.is_file():
        print(USAGE_INFO)
        sys.exit("ERROR: source file doesn't seem to exist")

if __name__ == '__main__':
    print(SOURCE_PATH)
