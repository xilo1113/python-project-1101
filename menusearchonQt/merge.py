from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import cv2
import numpy as np
a=''
options = Options()
options.add_argument("--disable-notifications")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless") #無頭模式
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome = webdriver.Chrome(executable_path='/Users/xilo1113/Downloads/chromedriver-1')
chrome.get('https://www.google.com.tw/maps')
searchbar=chrome.find_element(By.XPATH,'//*[@id="searchboxinput"]')
searchbar.send_keys(a)
searchbotton=chrome.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]')
searchbotton.click()
time.sleep(3)
urlnow=chrome.current_url
if 'search' in urlnow:
    firststore=chrome.find_element(By.XPATH,'//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/a')
    firststore.click()
else:
    pass
time.sleep(2)
picbotton=chrome.find_element(By.XPATH,'//*[@id="pane"]/div/div[1]/div/div/div[1]/div[1]/button/img')
picbotton.click()
time.sleep(1)
soup=BeautifulSoup(chrome.page_source, 'html.parser')
buttonlist=soup.find_all('div',{'class':"Gpq6kf gm2-button-alt"})
buttonlisttext=[]
for i in buttonlist:
    buttonlisttext.append(i.getText())
print(buttonlisttext)
menubotindex=buttonlisttext.index('菜單')

menubotton=chrome.find_element(By.XPATH,f'//*[@id="pane"]/div/div[1]/div/div/div[2]/div/div/button[{menubotindex+1}]')
menubotton.click()
time.sleep(1)
souhebutton=chrome.find_element(By.XPATH,'//*[@id="pane"]/div/div[3]/button')
souhebutton.click()
time.sleep(3)
chrome.save_screenshot("screenshot.png")

chrome.quit()


before=cv2.imread('screenshot.png')
after=before.copy()
b_channel, g_channel, r_channel = cv2.split(after)
alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
for i in range(1000):
    if b_channel[500,i]!=0:
        start=i
        break
for i in range(1000):
    if b_channel[500,2399-i]!=0:
        end=2399-i
        break
alpha_channel[:,:]=0
alpha_channel[:,start:end]=255
saved = cv2.merge((b_channel[:,start:end], g_channel[:,start:end], r_channel[:,start:end], alpha_channel[:,start:end]))

cv2.imwrite("noback.png", saved)
cv2.destroyAllWindows()
