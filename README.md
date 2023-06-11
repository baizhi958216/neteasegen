# 网易云听歌排行分析

## 1. 安装火狐浏览器以及geckodriver

- ArchLinux
    ```bash
    sudo pacman -S firefox geckodriver
    ```
- Windows
    只需要安装 [Firefox](https://www.mozilla.org/en-US/firefox/windows/)

## 2. 项目初始化

```bash
pip install -r requirements.txt
```

## 运行服务器

```bash
uvicorn server:app --reload
```

## 手动生成

### 生成csv文件
```bash
python neteasegen.py 网易云用户ID gencsv 输出文件路径
```

### 生成词云图

```bash
python neteasegen.py 网易云用户ID genwordcloud 输出文件路径
```

### 自定义背景词云图

```bash
python neteasegen.py 网易云用户ID gencustomcloud 自定义背景词路径 输出文件路径
```