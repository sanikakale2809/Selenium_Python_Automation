import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ops=Options()
ops.add_argument("--Headless")
driver = webdriver.Chrome(options=ops)
driver.get("https://google.com")
print(driver.title)
time.sleep(5)