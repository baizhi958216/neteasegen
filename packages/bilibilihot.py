from utils.annotation import log
import urllib.request
import json

@log("获取bilibili热榜")
def bilihot():
    api = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    req=urllib.request.Request(api)
    resp=urllib.request.urlopen(req)
    data=resp.read().decode('utf-8')
    return json.loads(data)