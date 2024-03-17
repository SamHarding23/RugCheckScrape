from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('headless') 
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu') 
options.add_argument('no-sandbox')  
options.add_argument('disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

url = 'https://example.com'

driver.get(url)

time.sleep(10)

html = driver.page_source

driver.quit()

soup = BeautifulSoup(html, 'html.parser')

good_elements = soup.find_all('h1', class_='mb-0 lg', string='Good')

if good_elements:
    print("Good")
else:
    print("Bad")
