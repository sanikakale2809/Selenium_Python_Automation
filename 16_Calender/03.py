import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.makemytrip.com/")
time.sleep(7)

#close login window
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
time.sleep(2)

#click on departure field
driver.find_element(By.XPATH,"(//span[@class='lbl_input appendBottom10'])[3]").click()
time.sleep(2)

expMonth="March 2027"
expDate="12"

#navigate to target month
while True:
    actMonth=driver.find_element(By.XPATH,"//div[@class='DayPicker-Caption']").text
    if actMonth==expMonth:
        break
    else:
        #click on next button
        driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
        time.sleep(1)

#Select date
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='dateInnerCell']//p[text()='"+expDate+"'])[1]").click()

time.sleep(20)