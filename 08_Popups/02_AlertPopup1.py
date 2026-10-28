import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)

#Enter Customer Id
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("1234")
time.sleep(2)

#Click on submit Button
driver.find_element(By.XPATH,"//input[@name='submit']").click()
time.sleep(2)

#getText from Alert Popups
Textvalue=driver.switch_to.alert.text
print(Textvalue)

#Click on cancel button from Alert Popup
# driver.switch_to.alert.dismiss()


#Click on Ok button from 1st Alert Popup
driver.switch_to.alert.accept()
time.sleep(2)

#Click on Ok button from 2ed Alert Popup
driver.switch_to.alert.accept()
time.sleep(2)