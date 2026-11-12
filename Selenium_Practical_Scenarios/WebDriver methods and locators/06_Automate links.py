# URL: https://the-internet.herokuapp.com/
# Test case:
# 1.Open the website.
# 2.Find all links using find_elements().
# 3.Print the total number of links.
# 4.Print the text of every link.
# 5.Find the link named Form Authentication.
# 6.Click the link.
# 7.Print the current URL.
# 8.Navigate back to the previous page.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get(" https://the-internet.herokuapp.com/")
time.sleep(5)


allLinks=driver.find_elements(By.XPATH,"//li")
print(len(allLinks))


for link in allLinks:
    print(link.text)
time.sleep(3)

autLink=driver.find_element(By.XPATH,"//a[text()='Digest Authentication']")
autLink.click()
time.sleep(3)
print("Current Url:",driver.current_url)
time.sleep(5)

driver.back()
time.sleep(3)
