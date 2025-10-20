from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'


def get_driver():

    # Inicia el driver de Chrome

    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
    return driver


def login_saucedemo(driver):

    driver.get (URL)

    # Esperar campo de usuario y completar formulario
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, 'user-name').send_keys(USERNAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()

     # Esperar redirección
    WebDriverWait(driver, 10).until(EC.url_contains('/inventory.html'))
   