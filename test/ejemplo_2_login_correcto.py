import selenium.webdriver as webdriver
import time
from selenium.webdriver.common.by import By


#Seccion A: preparar
driver = webdriver.Chrome()
driver.get("https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html")

#Seccion 2A: Ejecutar
#En nuestra pagina si tenemos definido cada campo con un "id" para cada uno, 
usuario = driver.find_element(By.ID,"usuario")
contrasena = driver.find_element(By.ID,"contra")
boton_Ingresar=driver.find_element(By.ID,"btnIngresar")

#Usando las credenciales de prueba para un administrador 
usuario.send_keys("admin@rom.com")
contrasena.send_keys("Adminrom1")
boton_Ingresar.click()


#Seccion 3A: Verificar
assert "Login" in driver.title
print("La página se ha cargado correctamente")
print("El título de la página es:", driver.title)
time.sleep(10)
#limpiar
driver.quit()