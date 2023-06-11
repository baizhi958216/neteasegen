import sys
from netease import getTop100
from csvgen import csvgenerator
from wordcloudgen import pngGeneratorByList

userId = sys.argv[1][7:]
command = sys.argv[2]
fileoutput = sys.argv[3]

songList = getTop100(userId)

if command=='gencsv':
    genRank = csvgenerator(songList,fileoutput)
elif command=='genwordcloud':
    pngGeneratorByList(songList,fileoutput)