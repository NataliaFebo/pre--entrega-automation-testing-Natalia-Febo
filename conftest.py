import os
import pytest
from datetime import datetime  


# Carpeta donde se guardan las capturas
SCREENSHOTS_DIR = os.path.join("reports", "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que se ejecuta después de cada test.
    Guarda una captura (pase o falle el test) en la carpeta 'reports/screenshots'.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        driver = item.funcargs.get("driver") #obtiene el fixture driver
        if driver:
            # Genera nombre del archivo
            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_file = os.path.join(SCREENSHOTS_DIR, f"{test_name}_{timestamp}.png")

            # Guardar la captura
            driver.save_screenshot(screenshot_file)
            print(f"\n Captura guardada: {screenshot_file}")

          
           



