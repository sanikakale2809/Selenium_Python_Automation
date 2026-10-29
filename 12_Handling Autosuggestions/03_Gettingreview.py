
# Search Redmi Note 15 mobile on Amazon and get the rating/review using XPath

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)

# Locate the search box using XPath and enter the mobile name
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("redmi note 15")
# Wait for autosuggestions to appear
time.sleep(5)

# Click the first autosuggestion using its XPath
driver.find_element(By.XPATH, "//div[@id='sac-suggestion-row-1']").click()
time.sleep(5)

# Locate the first matching element using XPath and get its visible text
rating = driver.find_element(By.XPATH, "//span[@class='a-size-mini a-color-base'][1]").text
print(rating)

driver.quit()
