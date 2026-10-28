import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

act=ActionChains(driver)

# Scroll down -> 1st Para: 0, 2nd Para: +ve   pixel values
act.scroll_by_amount(0,1000).perform()
time.sleep(3)

# Scroll up -> 1st Para: 0, 2nd Para: -ve   pixel values
act.scroll_by_amount(0,-600).perform()
time.sleep(3)

# Scroll right -> 1st Para: +ve, 2nd Para: 0   pixel values
# act.scroll_by_amount(300,0).perform()
# time.sleep(3)
#
# Scroll left -> 1st Para: -ve, 2nd Para: 0   pixel values
# act.scroll_by_amount(-150,0).perform()
# time.sleep(3)
