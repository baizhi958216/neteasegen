import csv
from utils.annotation import log

@log("生成CSV")
def csvgenerator(list:list,location:str='./TOP100.csv')->bool:

    csvFile = open(location,'w+',newline='',encoding='utf-8')

    writeStat = False

    try:
        writer = csv.writer(csvFile)
        writer.writerow(['songName','singerName'])
        for el in list:
            writer.writerow([el.get('songName'),el.get('singerName')])
        writeStat = True
    finally:
        csvFile.close()
        return writeStat