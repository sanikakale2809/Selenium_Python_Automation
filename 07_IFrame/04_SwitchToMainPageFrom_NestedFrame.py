import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

#Switch to outer frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))

#get text of outer frame
outerFrameText=driver.find_element(By.XPATH,"//p[text()='Outer iframe']").text
print(outerFrameText)

#Swicth to Inner/nested frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

#get text of Inner frame
InnerFrameText=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text
print(InnerFrameText)


# switch to main page from nested frame
driver.switch_to.default_content()

# driver.switch_to.parent_frame()
# driver.switch_to.parent_frame()


#get text of Home element from main page
HomeText=driver.find_element(By.XPATH,"(//a[text()='Home'])[1]").text
print(HomeText)



time.sleep(10)
