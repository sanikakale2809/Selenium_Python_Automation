import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


act=ActionChains(driver)

down=driver.find_element(By.XPATH,"//table[@name='BookTable']")
act.scroll_to_element(down).perform()
time.sleep(5)


SubjectNameofBook_learnJS=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[4]/td[3]").text
print(SubjectNameofBook_learnJS)


AuthorNameofBook_MasterJava=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[6]/td[2]").text
print(AuthorNameofBook_MasterJava)