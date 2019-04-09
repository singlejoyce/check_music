pyinstaller -i music.ico -F -w mainui.py -p checkmusic.py -p configreader.py -p logger.py --hidden-import checkmusic --hidden-import configreader --hidden-import logger
pause