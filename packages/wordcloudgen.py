from wordcloud import WordCloud
import numpy
from PIL import Image
from utils.annotation import log

@log('生成png格式词云图')
def pngGeneratorByList(list:list,output:str='./词云图.png'):
    word = []
    for li in list:
        word.append(li.get('songName').replace(' ',''))
        word.append(li.get('singerName').replace(' ',''))
    wordcloud = WordCloud(font_path='./libs/MiSans-Normal.ttf',width=1920,height=1080,background_color='#4f4f4f').generate(' '.join(word))
    wordcloud.to_image().save(output,'png')

@log('生成png格式自定义样式词云图')
def customPngGenByList(list:list,image:str,output:str='./词云图.png'):
    word = []
    for li in list:
        word.append(li.get('songName').replace(' ',''))
        word.append(li.get('singerName').replace(' ',''))
    wordcloud = WordCloud(
        mask=numpy.array(Image.open(image)),
        background_color='#FFFFFF',
        font_path='./libs/MiSans-Normal.ttf').generate(' '.join(word))
    wordcloud.to_image().save(output,'png')