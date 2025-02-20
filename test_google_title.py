import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
print("page title is", driver.title)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
time.sleep(5)