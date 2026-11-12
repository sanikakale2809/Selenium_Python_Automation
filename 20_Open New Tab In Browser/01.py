import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(5)


#Open New Tab
driver.execute_script("window.open('https://google.com');")
time.sleep(2)


# Switch to new tab
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.facebook.com")
time.sleep(2)

# Optional: switch back to original tab
driver.switch_to.window(driver.window_handles[0])


time.sleep(5)