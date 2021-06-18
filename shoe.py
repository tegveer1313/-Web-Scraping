from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  
path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.nike.com/in/launch/t/air-max-95-pineapple")
time.sleep(12)
#elements = driver.find_element_by_tag_name("li")
#elements.click()
xpath = "//button[text()='US 8']"
#wait_until_clickable(driver, xpath=xpath, duration=10)
driver.find_element_by_xpath(xpath).click()
#time.sleep(5)
zpath = "//button[text()='add to bag']"
driver.find_element_by_xpath(zpath).click()
#driver.find_element_by_class_name("ncss-btn-primary-dark  btn-lg capitalize").click()
time.sleep(10)

driver.quit()