import sys
from packages.netease import getTop100
from packages.csvgen import csvgenerator
from packages.wordcloudgen import pngGeneratorByList,customPngGenByList

userId = sys.argv[1][7:]
command = sys.argv[2]

songList = getTop100(userId)

if command=='gencsv':
    csvgenerator(songList,sys.argv[3])
elif command=='genwordcloud':
    pngGeneratorByList(songList,sys.argv[3])
elif command=='gencustomcloud':
    customPngGenByList(songList,sys.argv[3],sys.argv[4])