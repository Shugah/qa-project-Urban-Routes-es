from selenium.webdriver import Chrome, ChromeOptions
import data
from LandingPageMethods import (
    UrbanRoutesPage,
    ComfortRate,
    PhoneNumberSection,
    CreditCardSection,
    MessageForTheDriver,
    BlanketAndTissues,
    OrderTwoIceCreams,
    TaxiModal
)

class BaseTest:
    driver = None



    #Antes de TODOS los tests
    @classmethod
    def setup_class(cls):
        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = Chrome(options=options)
        cls.driver.get(data.urban_routes_url)








    # Antes de CADA test individual
    def setup_method(self):
        self.driver.delete_all_cookies()
        self.driver.get(data.urban_routes_url)

        #Establece ruta (desde, hasta)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)

        #Selecciona tarifa Comfort
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()




    #Se ejecuta una vez al final (cierre de navegador)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()







    #Prepara el flujo COMPLETO para TAXI y DRIVER modal
    def prepare_full_order(self):
        phone_section = PhoneNumberSection(self.driver)
        phone_section.phone_number()

        credit_card_section = CreditCardSection(self.driver)
        credit_card_section.credit_card()

        message = MessageForTheDriver(self.driver)
        message.write_message_to_driver()

        blanket_and_tissues = BlanketAndTissues(self.driver)
        blanket_and_tissues.switch_on()

        ice_creams = OrderTwoIceCreams(self.driver)
        ice_creams.click_plus_button()

        taxi = TaxiModal(self.driver)
        taxi.modal_to_search_taxi_appears()