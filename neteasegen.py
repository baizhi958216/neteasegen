import sys
from packages.netease import getTop100
from packages.csvgen import csvgenerator
from packages.wordcloudgen import pngGeneratorByList,customPngGenByList

try:
    if(sys.argv[1] and sys.argv[2]):
        songList = getTop100(sys.argv[1],False)
        if sys.argv[2]=='gencsv':
            csvgenerator(songList,sys.argv[3])
        elif sys.argv[2]=='genwordcloud':
            pngGeneratorByList(songList,sys.argv[3])
        elif sys.argv[2]=='gencustomcloud':
            customPngGenByList(songList,sys.argv[3],sys.argv[4])
except:
    print('参数不够\npython neteasegen.py 用户ID 生成格式 输出文件')
