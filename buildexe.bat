rem -F 表示生成单个可执行文件
rem -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
rem -p 表示你自己自定义需要加载的类路径，一般情况下用不到
rem -i 表示可执行文件的图标
pyinstaller -i music.ico mainui.py -p checkmusic.py -p configreader.py -p logger.py --hidden-import checkmusic --hidden-import configreader --hidden-import logger
pause