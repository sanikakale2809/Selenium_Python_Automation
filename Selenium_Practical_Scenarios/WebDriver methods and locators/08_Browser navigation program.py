# URL: https://www.wikipedia.org/
# Test case:
# 1.Open Wikipedia.
# 2.Print the page title.
# 3.Navigate to Google.
# 4.Print the page title.
# 5.Navigate back.
# 6.Navigate forward.
# 7.Refresh the page.
# 8.Minimize the browser.
# 9.Restore the browser.
# 10.Close it.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
time.sleep(4)

print("wikipedia page title:",driver.title)

time.sleep(3)

driver.get("https://google.com")
print("google page title:",driver.title)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.quit()