import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Asegura que Python encuentre la carpeta utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import login_saucedemo, get_driver



@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver() # instala el driver
    yield driver # mantiene la sesion iniciada
    driver.quit() #cierra la ventana



# Caso 1 - Login: Verifica redireccion e interfaz de inventario
def test_login(driver):
    login_saucedemo(driver)

    # Validación de URL
    assert "/inventory.html" in driver.current_url, "El login no redirigió correctamente."

    # Validación de Titulo
    titulo = driver.find_element(By.CSS_SELECTOR, "span.title").text #accede a el titulo
    assert titulo == 'Products', f"El título esperado era 'Products' pero se obtuvo '{titulo}'."



#  Caso 2 - Catálogo: Valida que haya productos visibles en la página de inventario y muestra nombre y precio del primero.
def test_catalogo(driver):
    login_saucedemo(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    #localiza la lista de productos
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    # Valida que la lista no este vacia, y muestra un mensaje de error por si falla
    assert len(products) > 0, "No se encontraron productos en el inventario."

    # Listar nombre y precio del primer producto
    first_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    # Imprime nombre y precio del primer producto
    print(f"Primer producto: {first_name} - {first_price}")



# Caso 3 - Carrito: Agrega productos y valida el contador del carrito.
def test_carrito(driver):
    login_saucedemo(driver)

    #Espera explícita: hasta que todos los elementos con la clase "inventory_item" estén presentes
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    # Obtiene lista de productos
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    total_productos = len(products)
    # Valida que al menos haya 2 productos para agregar al carrito
    assert total_productos >= 2, "No hay suficientes productos para realizar la prueba."

    # Agregar dos productos
    products[0].find_element(By.TAG_NAME, "button").click()
    products[1].find_element(By.TAG_NAME, "button").click()
  
    # Obtener el contador del carrito (badge) y validar que tenga 2 productos
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "2", f"Se esperaban 2 productos en el carrito, se obtuvo {badge}."
