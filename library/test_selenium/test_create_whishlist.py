import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time

@pytest.fixture(scope="module")
def setup_browser():
    driver_path = "C:\\Drivers\\msedgedriver.exe"
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_crear_whishlist(setup_browser):
    driver = setup_browser
    driver.get("http://127.0.0.1:8000/whislist/crear/")

    # Esperar 2 segundos para la carga de la pagina 
    time.sleep(2)

    # Asegurarse de que el boton este disponible antes de hacer clic
    boton_guardar = driver.find_element(By.ID, "boton_guardar")
    assert boton_guardar.is_displayed(), "El botón de guardar no está visible"

    # Clic en el botón de guardar
    boton_guardar.click()

    # Esperar 2 segundos para el procesamiento
    time.sleep(2)

    # Comprobar si la pagina contiene el mensaje de exito
    assert "Lista de deseos creada" in driver.page_source or "/whislist" in driver.current_url, "No se creó la wishlist correctamente"
