import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL= "https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html"
@pytest.fixture

def driver():
    d=webdriver.Chrome()
    yield d
    d.quit()
    
def test_carga_pagina(driver):
    driver.get(URL)
    assert driver.title == "Login - R.O.M."
    
def test_login_correcto(driver):
    driver.get(URL)
    usuario = driver.find_element(By.ID,"usuario")
    contrasena = driver.find_element(By.ID,"contra")
    boton_Ingresar=driver.find_element(By.ID,"btnIngresar")
    
    usuario.send_keys("admin@rom.com")
    contrasena.send_keys("Adminrom1")
    boton_Ingresar.click()
    time.sleep(3)
    
    try:
        assert "Login - R.O.M." in driver.current_url
    except :
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise
        
        
def test_login_incorrecto(driver):
    driver.get(URL)
    usuario = driver.find_element(By.ID,"usuario")
    contrasena = driver.find_element(By.ID,"contra")
    boton_Ingresar=driver.find_element(By.ID,"btnIngresar")

    usuario.send_keys("correoPrueba@rom.com")
    contrasena.send_keys("123")
    boton_Ingresar.click()
    time.sleep(3)
    
    try:
        assert driver.find_element(By.ID,"mensaje").text == "Correo o contraseña incorrectos"
        
    except:
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise
        