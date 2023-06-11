import time
from packages.netease import getTop100
from packages.csvgen import csvgenerator
from packages.wordcloudgen import pngGeneratorByList,customPngGenByList

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles

from starlette.responses import RedirectResponse

app = FastAPI()

# 静态资源目录挂载
app.mount("/static", StaticFiles(directory="static"), name="static")

# 重定向至我的github page
@app.get("/")
async def root():
    return RedirectResponse(url='https://baizhi958216.github.io')

# 生成csv
@app.get('/gencsv/{userId}',status_code=200)
async def gencsv(userId):
    songList = getTop100(userId)
    filePath = './static/'+userId+'.csv'
    csvgenerator(songList,filePath)
    return { 'userId' : userId, 'filePath' : userId+'.csv' }

# 生成默认词云图
@app.get('/genwordcloudpng/{userId}',status_code=200)
async def genwordcloudpng(userId):
    songList = getTop100(userId)
    filePath = './static/'+userId+'.png'
    pngGeneratorByList(songList,filePath)
    return { 'userId' : userId, 'filePath' : userId+'.png' }

@app.post('/gencustomcloudpng',status_code=200)
async def gencustomcloudpng(
    imagefile: UploadFile = File(), userId: str = Form()
):
    # 缓存一份用户上传图像
    contents = await imagefile.read()
    usercustomimage = userId+str(time.time())
    with open('./static/'+usercustomimage,'wb') as binary:
        binary.write(contents)
    # 生成词云
    songList = getTop100(userId)
    filePath = './static/'+userId+'.png'
    customPngGenByList(songList,'./static/'+usercustomimage,filePath)
    return { 'userId' : userId, 'filePath' : userId+'.png' }