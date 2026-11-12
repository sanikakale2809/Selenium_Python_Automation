# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Find all input fields using find_elements().
# 2.Print the total number of input fields.
# 3.Print the tag name of each input element.
# 4.Find the name field and enter a value.
# 5.Find the email field and enter a value.
# 6.Check whether the fields are displayed and enabled.
# 7.Print the results.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

allField=driver.find_elements(By.XPATH,"//input")
print(len(allField))

for field in allField:
    print(field.tag_name)

Name=driver.find_element(By.XPATH,"//input[@id='name']")
Email=driver.find_element(By.XPATH,"//input[@id='email']")
Name.send_keys("Sanika Kale")
Email.send_keys("Sanika@gmail.com")
time.sleep(5)

print("Name field is displayed:",Name.is_displayed())
print("Email field is displayed:",Email.is_displayed())

if Name.is_displayed()==True and Email.is_displayed()==True:
    print("Pass")
else:
    print("Fail")