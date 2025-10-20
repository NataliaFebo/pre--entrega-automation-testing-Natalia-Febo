# Pre-Entrega Proyecto Automation Testing - Natalia Febo

## Objetivo
Automatizar los flujos básicos de navegación web en [SauceDemo](https://www.saucedemo.com) utilizando Selenium WebDriver y Python, incluyendo:

- Login con usuario válido.
- Verificación del catálogo de productos.
- Interacción con el carrito de compras.
- Capturas automáticas de pantalla en cada test, pase o falle.
- Generación de reportes HTML


## Tecnologías
- Python 3.13.7
- Selenium WebDriver
- Pytest
- pytest-html
- webdriver-manager


##  Estructura del Proyecto

pre-entrega-automation-testing-Natalia-Febo/

* test/
    -test_saucedemo.py         # Tests automatizados

* utils/
    -helpers.py                # Funciones auxiliares (login, driver)

* reports/
    -reporte.html              # Reporte HTML generado
    -screenshots/              # Capturas automáticas de cada test

* conftest.py                   # Fixture y hook para screenshots
* requirements.txt              # Dependencias del proyecto
* README.md                     # Este archivo



## Instalación de Dependencias

-Ubicarse en la carpeta raiz del proyecto y ejecutar
`pip install -r requirements.txt`

O instalandolo de forma individual:

- pip install selenium
- pip install pytest
- pip install pytest-html
- pip install webdriver-manager


##  Ejecución de los Tests

- bash
pytest test/test_saucedemo.py -v --html=reports/reporte.html


- `-v` - modo verbose, muestra el detalle de cada test.
- `--html=reports/reporte.html` - genera el reporte HTML en la carpeta `reports`.



##  Capturas de Pantalla

- Cada test genera automáticamente una captura de pantalla, pase o falle.

- Las capturas se guardan en: reports/screenshots/




##  Abrir el Reporte HTML

1. Navegá a la carpeta `reports`.
2. Hacer click derecho sobre documento 'reporte.html'
3. Hacer click sobre 'Reveal in File Explorer
4. Hacer doble click sobre el link 'reporte'
5. Se mostrará en tu navegadorel reporte con el estado de cada test.

