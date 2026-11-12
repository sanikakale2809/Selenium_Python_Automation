import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/date-picker")
time.sleep(5)


#Click on date field
driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']").click()
time.sleep(5)

yearValue="2004"
monthValue="September"
dayValue="28"

#Select year
year=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
s1=Select(year)
s1.select_by_visible_text(yearValue)
time.sleep(2)

#Select month
month=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
s2=Select(month)
s2.select_by_visible_text(monthValue)
time.sleep(2)

#select date
driver.find_element(By.XPATH,"//div[text()='"+dayValue+"']").click()
time.sleep(20)
