import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/date-picker")
time.sleep(5)


#Click on date field
driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']").click()
time.sleep(5)


#Select year
year=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
s1=Select(year)
s1.select_by_value("2004")
time.sleep(2)


#Select month
month=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
s1=Select(month)
s1.select_by_value("9")
time.sleep(2)


#select date
driver.find_element(By.XPATH,"//div[text()='28']").click()
time.sleep(5)

