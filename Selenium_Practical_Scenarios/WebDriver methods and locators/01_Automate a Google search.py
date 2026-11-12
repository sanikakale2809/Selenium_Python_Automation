# URL: https://www.google.com/
# Test case:
# 1.Launch Chrome browser.
# 2.Maximize the browser.
# 3.Open Google.
# 4.Print the page title and current URL.
# 5.Find the search box using a suitable locator.
# 6.Enter Selenium Python.
# 7.Submit the search.
# 8.Print the title of the result page.
# 9.Close the browser.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)


print("Page Title:", driver.title)
print("Page URL:", driver.current_url)


searchBox=driver.find_element(By.CLASS_NAME,'gLFyf')
searchBox.send_keys("Selenium Python")
searchBox.submit()
time.sleep(5)

print("The title of the result Page:", driver.title)
driver.quit()
