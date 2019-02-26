pyinstaller -i music.ico layout.py -p checkmusic.py -p configreader.py -p logger.py --hidden-import checkmusic --hidden-import configreader --hidden-import logger
pause