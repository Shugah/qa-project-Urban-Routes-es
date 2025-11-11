import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from retrieve_phone_code import retrieve_phone_code



class UrbanRoutesPage:
    from_field = (By.XPATH, "//input[@id='from']")
    to_field = (By.XPATH, "//input[@id='to']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')



#ALL FOR ONE. Rellenar desde y hasta.
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)






class ComfortRate:
    order_taxi = (By.XPATH, "//button[@type='button' and contains(text(), 'Pedir un taxi')]")
    comfort_taxi = (By.XPATH, "//img[@alt='Comfort']")
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    comfort_taxi_active = (By.CLASS_NAME, "tcard.active")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_order_taxi(self):
        self.wait.until(EC.visibility_of_element_located(self.order_taxi)).click()

    def click_comfort_taxi(self):
        self.wait.until(EC.visibility_of_element_located(self.comfort_taxi)).click()


    def get_current_selected_plan(self):
        return self.driver.find_element(*self.active_plan_card).text



            #ALL FOR ONE. Seleccionar la tarifa comfort
    def select_comfort_taxi(self):
        self.click_order_taxi()
        self.click_comfort_taxi()








class PhoneNumberSection:
    phone_trigger = (By.CLASS_NAME, 'np-text')
    phone_input = (By.ID, 'phone')
    siguiente_button = (By.XPATH, '//button[@type="submit" and text()="Siguiente"]')
    code_input = (By.ID, "code")
    confirmar_button = (By.XPATH, '//button[@type="submit" and text()="Confirmar"]')
    phone_active = (By.CLASS_NAME, "np-text")



    def __init__(self, driver):
        self.driver = driver

    def click_phone_trigger(self):
        self.driver.find_element(*self.phone_trigger).click()

    def add_phone_input(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)

    def click_siguiente_button(self ):
        self.driver.find_element(*self.siguiente_button).click()

    def add_code_return(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.code_input).send_keys(code)

    def click_confirmar_button(self):
        self.driver.find_element(*self.confirmar_button).click()

    def phone_status(self):
        return self.driver.find_element(*self.phone_active)




            #ALL FOR ONE. Rellenar numero de telefono
    def phone_number(self):
        self.click_phone_trigger()
        self.add_phone_input()
        self.click_siguiente_button()
        self.add_code_return()
        self.click_confirmar_button()



class CreditCardSection:
    payment_method = (By.CLASS_NAME, 'pp-button')
    add_credit_card = (By.CLASS_NAME, 'pp-plus-container')
    card_number = (By.ID, 'number')
    card_code = (By.ID, "code")
    agregar_button = (By.XPATH, '//button[@type="submit" and text()="Agregar"]')
    close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    credit_card_status = (By.CLASS_NAME, 'pp-value-text')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_card_trigger(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_credit_card(self):
        self.driver.find_element(*self.add_credit_card).click()

    def add_card_number(self):
        field = self.wait.until(EC.element_to_be_clickable(self.card_number))
        field.click()
        field.send_keys(data.card_number)
        field.send_keys(Keys.TAB+data.card_code)

    def click_agregar_button(self):
        self.driver.find_element(*self.agregar_button).click()

    def click_close_button(self):
        self.driver.find_element(*self.close_button).click()

    def card_status(self):
        return self.driver.find_element(*self.credit_card_status)



#ALL FOR ONE. Agregar una tarjeta de crédito
    def credit_card(self):
        self.click_card_trigger()
        self.click_add_credit_card()
        self.add_card_number()
        self.click_agregar_button()
        self.click_close_button()



class MessageForTheDriver:
    driver_message_field = (By.ID, 'comment')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def message_to_driver(self):
        self.driver.find_element(*self.driver_message_field).send_keys(data.message_for_driver)

    def message_status(self):
        return  self.wait.until(EC.presence_of_element_located(self.driver_message_field))


            #ALL FOR ONE. Escribir un mensaje para el conductor.
    def write_message_to_driver(self):
        self.message_to_driver()



class   BlanketAndTissues:
    switch = (By.CLASS_NAME, "slider")
    option_switches = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def switch_enabled(self):
        self.driver.find_element(*self.switch).click()

    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = self.driver.find_elements(*self.option_switches_inputs)
        return switches[0].get_property('checked')



            #ALL FOR ONE. Pedir una manta y pañuelos.
    def switch_on(self):
        self.driver.find_element(*self.switch).click()




class OrderTwoIceCreams:
    plus_button = (By.XPATH, "//div[@class='r-counter']//div[@class='counter-plus']")
    ice_creams_units = (By.XPATH, "//div[@class='r-counter']//div[@class='counter-value']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_plus_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.plus_button))
        option_add_controls = self.driver.find_elements(*self.plus_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", option_add_controls[0])
        option_add_controls[0].click()
        option_add_controls[0].click()


    def get_units(self):
        element = self.wait.until(EC.visibility_of_element_located(self.ice_creams_units))
        return element.text

    # ALL FOR ONE. Pedir 2 helados.
    def order_ice_creams(self):
        self.click_plus_button()





class TaxiModal:
    modal_trigger_button = (By.XPATH, "//span[@class='smart-button-main' and text()='Pedir un taxi']")
    modal_expected = (By.CLASS_NAME, "order-header-title")



    def __init__(self, driver):
        self.driver = driver

    def modal(self):
        self.driver.find_element(*self.modal_trigger_button).click()

    def taxi_modal(self):
        return self.driver.find_element(*self.modal_expected)


            #ALL FOR ONE
    def modal_to_search_taxi_appears(self):
        self.modal()





class DriverModal:
    driver_modal_section = (By.CLASS_NAME, "order-header-title")
    driver_name = (By.CSS_SELECTOR, ".order.shown .order-button[style*='cursor']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 28)
        self.sleep = time.sleep

    def a_wait(self, seconds=13):
        time.sleep(seconds)

    def driver_modal(self):
        return self.wait.until(EC.visibility_of_element_located(self.driver_modal_section))

    def is_driver_name_visible(self):
        return self.driver.find_element(*self.driver_name).is_displayed()

    def driver_modal_appears(self):
        self.a_wait()
        self.driver_modal()