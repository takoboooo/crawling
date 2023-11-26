from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# 設定瀏覽器選項
options = Options()
# 建立 driver
s = Service(r"INPUT DRIVER PATH HERE")
chrome = webdriver.Chrome(service=s, options=options)
# 存取 Website
url = "https://www.ncu.edu.tw/tw/"
chrome.get(url)
# 等待 5 秒鐘以載入頁面
time.sleep(5)
# 關閉瀏覽器視窗
chrome.close()