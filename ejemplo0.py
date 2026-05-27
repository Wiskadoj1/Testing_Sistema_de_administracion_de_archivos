from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  
#"driver": Navegador
driver=webdriver.Chrome()
driver.get("https://www.google.com/")

busqueda = driver.find_element(By.NAME,"q")
busqueda.send_keys("Facultad de ingeniería")

time.sleep(5)
busqueda.send_keys(Keys.ENTER)


driver.quit()