import sys
from packages.netease import getTop100
from packages.csvgen import csvgenerator
from packages.wordcloudgen import pngGeneratorByList

userId = sys.argv[1][7:]
command = sys.argv[2]
fileoutput = sys.argv[3]

songList = getTop100(userId)

if command=='gencsv':
    csvgenerator(songList,fileoutput)
elif command=='genwordcloud':
    pngGeneratorByList(songList,fileoutput)