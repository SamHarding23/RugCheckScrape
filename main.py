from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://rugcheck.xyz/tokens/AZFrPdoVHS8c4y1rkVUnPUQQdbWdvxMiXSBrqYf7jgce'

driver.get(url)

time.sleep(10)


html = driver.page_source

driver.quit()


soup = BeautifulSoup(html, 'html.parser')

good_elements = soup.find_all('h1', class_='mb-0 lg', string='Good')

if good_elements:
    print(url, ": Good")
else:
    print(url, ": Bad")
