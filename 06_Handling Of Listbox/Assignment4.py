
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()                                             # Create WebDriver object
driver.maximize_window()                                                # Maximize browser window
driver.get("https://testautomationpractice.blogspot.com/")              # Call URL / Open website
time.sleep(2)


print("========== Colors Listbox ==========")

colors = driver.find_element(By.XPATH, "//select[@id='colors']")
s = Select(colors)                                                      # Create Select class object
allOption = s.options                                                   # Get all options from Colors listbox
all_Option = []                                                         # Create an empty list to store option text

for Option in allOption:                                                # Extract text of each option and append it to the list
    all_Option.append(Option.text)

all_Option.sort()                                                       # Sort all color names in alphabetical order

for color in all_Option:                                                # Print each color separately
    print(color)


print("========== Country Listbox ==========")

country = driver.find_element(By.XPATH, "//select[@id='country']")
s = Select(country)                                                     # Create Select class object for Country listbox
allOption = s.options                                                   # Get all options from Country listbox
all_Option = []                                                         # Create an empty list to store option text

for option in allOption:                                                # Extract text of each option and append it to the list
    all_Option.append(option.text)

all_Option.sort()                                                       # Sort all country names in alphabetical order

for country in all_Option:                                              # Print each country separately
    print(country)

driver.quit()


