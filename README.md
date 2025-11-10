# Proyecto de Pruebas Automatizadas — Urban Routes 🚘

## Descripción
Este proyecto contiene pruebas automatizadas para la aplicación Urban Routes.  
Las pruebas están desarrolladas en **Python** utilizando **Pytest** y **Selenium WebDriver**, organizadas en **clases y métodos** para mantener una estructura clara, escalable y reutilizable.

---
## Organización del Código

El proyecto sigue una arquitectura basada en **Page Object Model (POM)**:

### Clases de Métodos (Methods.py)
Contienen las acciones que se realizan sobre los elementos de la interfaz.

Ejemplo:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

---

### Clases de Pruebas (Tests.py)
Usan los métodos definidos anteriormente para crear flujos de prueba completos.

import pytest
from LandingPageMethods import LandingPageMethods

    class TestUrbanRoutes:
        def test_order_taxi(self, driver):
            page = LandingPageMethods(driver)
            page.click_taxi_button()
            assert "Pedido confirmado" in driver.page_source

---

## Requisitos Previos

- Python 3.10 o 3.13 si es posible.
- Navegador (Google Chrome en este caso)  
- ChromeDriver instalado  
- PyCharm 

---

## Instalación del Entorno

- Clona el repositorio:  

git clone https://github.com/Shugah/qa-project-Urban-Routes-es.git

git clone git@github.com:Shugah/qa-project-Urban-Routes-es.git

cd qa-project-Urban-Routes-es

## 👩‍💻 Autor

**Honey Ochoa**  
Proyecto de automatización QA — Urban Routes (versión en español)


---


# Automated Testing Project — Urban Routes 🚘

## Description
This project contains automated tests for the **Urban Routes** application.  
The tests are developed in **Python** using **Pytest** and **Selenium WebDriver**, organized into **classes and methods** to maintain a clear, scalable, and reusable structure.

---

## Code Organization

The project follows a **Page Object Model (POM)** architecture:

### Method Classes (Methods.py)
Contain the actions performed on the interface elements.

Example:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    class UrbanRoutesPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)

        def set_from(self, from_address):
            self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

---

### Test Classes (Tests.py)
Use the previously defined methods to create complete test flows.

import pytest
from LandingPageMethods import LandingPageMethods

    class TestUrbanRoutes:
        
        def test_order_taxi(self, driver):
            page = LandingPageMethods(driver)
            page.click_taxi_button()
            assert "Order confirmed" in driver.page_source

---

## Prerequisites

- Python 3.10 (or 3.13 if possible)  
- Web browser (Google Chrome in this case)  
- ChromeDriver installed  
- PyCharm  

---

## Environment Setup

- Clone the repository:  

git clone https://github.com/Shugah/qa-project-Urban-Routes-es.git  

git clone git@github.com:Shugah/qa-project-Urban-Routes-es.g

cd qa-project-Urban-Routes-es

## 👩‍💻 Author

**Honey Ochoa**  
QA Automation Project — Urban Routes (English version).