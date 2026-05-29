from selenium import webdriver

#A - Preparar 
driver = webdriver.Chrome()

#A - Ejecutar
driver.get("https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html")

#A - Verificar

assert "Login" in driver.title
print("El sistema cargó correctamente :)")
print ("El título de la página es: " + driver.title)

#Limpiar
driver.quit()