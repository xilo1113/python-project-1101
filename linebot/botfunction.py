from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os 
import time
def helpmes():
    return '指令列表:\n以 ! 開頭搜文章'
def blogadvise(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    chrome.get('https://ifoodie.tw/search?q='+keyword)
    time.sleep(3)
    soup=BeautifulSoup(chrome.page_source, 'html.parser')
    centerlist=soup.find_all('a',{'class':'readmore'})
    purelist=[]
    for htmlsource in centerlist:
        purelist.append(htmlsource['href'])
    mes='安食記'
    for i in purelist:
        mes+='\n'+i[30:]
        mes+='\n'+'https://ifoodie.tw'+i[0:30]
    chrome.quit()
    return mes