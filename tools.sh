#!/bin/bash

SCRIPT_NAME=`basename "$0"`

if [ $1 = "build" ]; then #https://pyinstaller.readthedocs.io/en/stable/
    sh $SCRIPT_NAME test
    #pyinstaller index.py
    pyinstaller --onefile --windowed index.py
#elif [ $1 = "cythonize" ]; then
    #sh $SCRIPT_NAME test
    #python build.py build_ext --inplace
elif [ $1 = "test" ]; then
    coverage run -m --source=. pytest tests.py -v
    coverage html
    pipreqs --savepath requirements.txt
fi
