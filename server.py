import time
from packages.netease import getTop100
from packages.csvgen import csvgenerator
from packages.wordcloudgen import pngGeneratorByList,customPngGenByList
from packages.bilibilihot import bilihot

from typing import Annotated
from fastapi import FastAPI, File, Form
from fastapi.staticfiles import StaticFiles

from starlette.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 跨域处理

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态资源目录挂载
app.mount("/static", StaticFiles(directory="static"), name="static")

# 重定向至我的github page
@app.get("/",summary='重定向至我的github page')
async def root():
    return RedirectResponse(url='https://baizhi958216.github.io')

# 生成csv
@app.get(
        '/gencsv/{userId}',
        status_code=200,
        summary='生成CSV文件'
        )
async def gencsv(userId):
    songList = getTop100(userId)
    filePath = './static/'+userId+'.csv'
    csvgenerator(songList,filePath)
    return { 'userId' : userId, 'filePath' : userId+'.csv' }

# 生成默认词云图
@app.get(
        '/genwordcloudpng/{userId}',
        status_code=200,
        summary="生成词云图"
        )
def genwordcloudpng(userId):
    songList = getTop100(userId,False)
    fileName = str(time.time())
    filePath = './static/'+fileName+'.png'
    pngGeneratorByList(songList,filePath)
    return { 'userId' : userId, 'filePath' : fileName+'.png' }

@app.post(
        '/gencustomcloudpng',
        status_code=200,
        description="生成自定义背景的词云图, 词云图大小为上传图片大小",
        summary="上传图片，该图片作为词云图背景"
        )
def gencustomcloudpng(
    imagefile: Annotated[bytes, File()], userId: Annotated[str, Form()]
):
    # 缓存一份用户上传图像
    usercustomimage = userId+str(time.time())
    with open('./static/'+usercustomimage,'wb') as binary:
        binary.write(imagefile)
    # 生成词云
    songList = getTop100(userId, False)
    fileName = str(time.time())
    filePath = './static/'+fileName+'.png'
    customPngGenByList(songList,'./static/'+usercustomimage,filePath)
    return { 'userId' : userId, 'filePath' : fileName+'.png' }

@app.get('/getweek/{userId}',status_code=200,
        summary="所有周排行信息")
def getweek(userId):
    songList = getTop100(userId,True)
    fileName = str(time.time())
    filePath = './static/'+fileName+'.png'
    pngGeneratorByList(songList,filePath)
    return { 'userId' : userId, 'filePath' : fileName+'.png' }

@app.post(
        '/getcustomweek',
        status_code=200,
        description="生成自定义背景的词云图, 词云图大小为上传图片大小",
        summary="上传图片，该图片作为词云图背景"
        )
def gencustomcloudpngweek(
    imagefile: Annotated[bytes, File()], userId: Annotated[str, Form()]
):
    # 缓存一份用户上传图像
    usercustomimage = userId+str(time.time())
    with open('./static/'+usercustomimage,'wb') as binary:
        binary.write(imagefile)
    # 生成词云
    songList = getTop100(userId, True)
    fileName = str(time.time())
    filePath = './static/'+fileName+'.png'
    customPngGenByList(songList,'./static/'+usercustomimage,filePath)
    return { 'userId' : userId, 'filePath' : fileName+'.png' }

@app.get('/bilibilihot',status_code=200,summary='哔哩哔哩热搜')
def hot():
    return bilihot()