from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() 

try:
    driver.get("https://the-internet.herokuapp.com/login")
    
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("muhammedKumcu")
    password.send_keys("123456789")
    password.send_keys(Keys.RETURN)

    driver.save_screenshot("../ekranGoruntusu.png")

finally:
    driver.quit()
