import selenium.webdriver as webdriver
import time

#Seccion A: preparar
driver = webdriver.Chrome()

#Seccion 2A: Ejecutar
driver.get("https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html")


#Seccion 3A: Verificar
assert "Login" in driver.title
print("La página se ha cargado correctamente")
print("El título de la página es:", driver.title)
time.sleep(50)
#limpiar
driver.quit()
