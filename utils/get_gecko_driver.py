from win32com.client import Dispatch
import os
import pathlib
import requests
import pythoncom
import zipfile
from utils.annotation import log

@log("获取geckodriver")
def get_gecko_driver():
    pythoncom.CoInitialize()

    # 获取Chrome版本
    # parser = Dispatch("Scripting.FileSystemObject")
    # version = parser.GetFileVersion(
    #     r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    # 获取Edge版本
    # parser = Dispatch("Scripting.FileSystemObject")
    # version = parser.GetFileVersion(
    #     r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

    # 获取FireFox版本
    # parser = Dispatch("Scripting.FileSystemObject")
    # version = parser.GetFileVersion(
    #     r"C:\Program Files\Mozilla Firefox\firefox.exe")
    
    # chromedriver下载链接
    # chromeAPI = f"https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip"

    # msedgedriver下载链接
    # edgeAPI = f"https://msedgedriver.azureedge.net/{version}/edgedriver_win64.zip"
    
    # geckodriver下载链接
    firefoxAPI = f"https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip"

    # 下载到当前路径
    BASE_DIR = str(pathlib.Path.cwd())

    BROWSER_DRIVER_DIR = str(pathlib.PurePath(
        BASE_DIR, "geckodriver-v0.33.0-win64.zip"))

    download_dir = os.path.join(str(BROWSER_DRIVER_DIR))

    if os.access('libs/geckodriver.exe',os.F_OK):
        print('geckodriver.exe存在...')
        pythoncom.CoUninitialize
        return
    else:
        print('geckodriver.exe不存在, 开始下载...')
        resp = requests.get(firefoxAPI, stream=True)

        with open(download_dir, 'wb') as fo:
            fo.write(resp.content)

        # 解压geckodriver到libs
        zip_file = zipfile.ZipFile('geckodriver-v0.33.0-win64.zip')
        for names in zip_file.namelist():
            zip_file.extract(names,'libs')
        zip_file.close()

    pythoncom.CoUninitialize
