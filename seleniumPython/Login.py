import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="F:\\Python\\chromedriver.exe")
print(type(driver))

driver.get("https://www.daraz.com.bd/")

driver.maximize_window()
time.sleep(8)

link = driver.find_element_by_link_text("SIGNUP / LOGIN")
link.click()
driver.find_element(By.XPATH"This element might be inside iframe from different src. Currently ChroPath doesn't support for them."]
driver.quit()