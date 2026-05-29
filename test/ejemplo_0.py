from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(1)

busqueda = driver.find_element(By.NAME, "q")
busqueda.send_keys("Facultad de ingeniería UNAM")

time.sleep(1)

busqueda.send_keys(Keys.ENTER)
time.sleep(7)
driver.quit()