# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Open the website.
# 2.Find the buttons using CSS selector.
# 3.Print the number of buttons.
# 4.Print the text of each button.
# 5.Check whether a particular button is displayed and enabled.
# 6.Click the button.
# 7.Print the result.



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

Buttons=driver.find_elements(By.XPATH,"//button")
print(len(Buttons))

for Button in Buttons:
    print(Button.text)
time.sleep(3)


Btn=driver.find_element(By.CSS_SELECTOR,"*#alertBtn")

print("Simple Alert button is displayed:",Btn.is_displayed())
print("Simple Alert button is enabled:",Btn.is_enabled())


if Btn.is_displayed() and Btn.is_enabled():
    Btn.click()
    print("Button clicked successfully")
else:
    print("Button is not clickable")