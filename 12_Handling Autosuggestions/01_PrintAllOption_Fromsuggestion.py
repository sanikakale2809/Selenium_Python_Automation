import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(5)


driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("samsung")
time.sleep(2)


allOptions=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]//li")


for eachOption in allOptions:
    value=eachOption.text
    print(value)

time.sleep(2)