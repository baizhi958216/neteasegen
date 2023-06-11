from wordcloud import WordCloud
from annotation import log

log('生成歌单词云图...')
def pngGeneratorByList(list:list,output:str='./词云图.png'):
    word = []
    for li in list:
        word.append(li.get('songName'))
        word.append(li.get('singerName'))
    wordcloud = WordCloud(font_path='/usr/share/fonts/misans/MiSans-Normal.ttf',width=1920,height=1080).generate(' '.join(word))
    wordcloud.to_image().save(output,'png')