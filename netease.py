from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from annotation import log

@log("获取歌单...")
def getTop100(userId:str)->list:

    # 启动无GUI式webdriver
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    driver.get("https://music.163.com/#/user/songs/rank?id="+userId)

    # 网易云h5端使用iframe渲染
    driver._switch_to.frame('g_iframe')

    # 获取所有时间的歌曲排行
    allTime = driver.find_element(By.ID,'songsall')
    allTime.click()

    # 等待排行榜完成渲染
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,'ttc')))

    elements = driver.find_elements(By.CLASS_NAME,'ttc')

    songsList = []

    for el in elements:
        index = el.text.find(' -')
        songData  = {}
        songData['songName'] = el.text[0:index]
        songData['singerName']  = el.text[index+2:len(el.text)]
        songsList.append(songData)

    driver.close()

    return songsList