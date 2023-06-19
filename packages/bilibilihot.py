from utils.annotation import log
import urllib.request
import json

@log("获取bilibili热榜")
def bilihot(ranksize:int=10):
    api = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    req=urllib.request.Request(api)
    resp=urllib.request.urlopen(req)
    rawdata=resp.read().decode('utf-8')
    rawList = json.loads(rawdata)['data']['list']

    data=[]
    
    for index in range(len(rawList)):
        if index>=ranksize:
            return data
        else:
            item = {}
            item['tname'] = rawList[index]['tname']
            item['title'] = rawList[index]['title']
            item['view'] = rawList[index]['stat']['view']
            item['danmaku'] = rawList[index]['stat']['danmaku']
            item['reply'] = rawList[index]['stat']['reply']
            item['favorite'] = rawList[index]['stat']['favorite']
            item['coin'] = rawList[index]['stat']['coin']
            item['like'] = rawList[index]['stat']['like']
            item['bvid'] = rawList[index]['bvid']
            data.append(item)

    return data