import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()
    
def test_carga_pagina(driver):
    driver.get(URL)
    assert "Login - R.O.M" in driver.title
    time.sleep(1)
     
def test_login_correcto(driver):
    driver.get(URL)
    usuario = driver.find_element(By.ID, "usuario")
    contrasena = driver.find_element(By.ID, "contra")
    boton_Ingresar = driver.find_element(By.ID, "btnIngresar")
    
    usuario.send_keys("admin@rom.com")
    contrasena.send_keys("Adminrom1")
    boton_Ingresar.click()
    time.sleep(1)
    
    try:
        mensaje_bienvenida = driver.find_element(By.ID, "mensaje").text
        
        assert "Bienvenido al sistema Administrador" in mensaje_bienvenida
    except:
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/test_correcto.png")
        raise
        
def test_login_incorrecto(driver):
    driver.get(URL)
    usuario = driver.find_element(By.ID, "usuario")
    contrasena = driver.find_element(By.ID, "contra")
    boton_Ingresar = driver.find_element(By.ID, "btnIngresar")

    usuario.send_keys("correoPrueba@rom.com")
    contrasena.send_keys("123")
    boton_Ingresar.click()
    time.sleep(3)
    
    try:
    
        mensaje_error = driver.find_element(By.ID, "mensaje").text
        assert mensaje_error == "Bienvenido al sistema Administrador"
        
    except:
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise
def test_registrar(driver):
    driver.get(URL)
    
    boton_ir_a_registro = driver.find_element(By.LINK_TEXT, "¿No te has registrado? Hazlo aqui")
    boton_ir_a_registro.click()
    time.sleep(3)
    
    ingresa_nombre= driver.find_element(By.ID, "nombre")
    ingresa_correo= driver.find_element(By.ID, "correo")
    ingresa_contra= driver.find_element(By.ID, "contraseña")
    
    boton_registrase = driver.find_element(By.ID, "btnRegistrar")
    
    ingresa_nombre.send_keys("General Valencia")
    ingresa_correo.send_keys("general.valencia@rom.com")
    ingresa_contra.send_keys("Generalrom1")
    
    
    boton_registrase.click()
    time.sleep(2)
    
    try:
        mensaje_registro = driver.find_element(By.ID, "mensaje").text
        assert mensaje_registro == "Usuario registrado correctamente"
        driver.save_screenshot("evidencias/test_registrar.png")
        
    except:
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/test_registrar.png")
        raise

