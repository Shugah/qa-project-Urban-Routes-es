from LandingPageMethods import UrbanRoutesPage
from LandingPageMethods import ComfortRate
from LandingPageMethods import PhoneNumberSection
from LandingPageMethods import CreditCardSection
from LandingPageMethods import MessageForTheDriver
from LandingPageMethods import BlanketAndTissues
from LandingPageMethods import OrderTwoIceCreams
from LandingPageMethods import TaxiModal
from LandingPageMethods import DriverModal
import data
from selenium.webdriver import Chrome, ChromeOptions





#T E S T S
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono


        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = Chrome(options=options)
        cls.driver.get("https://cnt-9458d928-bb5f-4933-9ca3-a2d0a0284b05.containerhub.tripleten-services.com?lng=es")


                                                #T E S T S


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to




    def test_comfort_rate(self):
        #Test se prepara
        self.driver.get(data.urban_routes_url)
        rates_page = ComfortRate(self.driver)

        #Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

        ##Test finaliza
        rates_page.select_comfort_taxi()
        comfort_rate_status = rates_page.comfort_status()
        assert "active" in comfort_rate_status.get_attribute("class")




    def test_phone_number(self):
        self.driver.get(data.urban_routes_url)
        phone_section = PhoneNumberSection(self.driver)


        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()


        phone_section.phone_number()
        assert "+1" in phone_section.phone_status().text




    def test_credit_card(self):
        self.driver.get(data.urban_routes_url)
        credit_card_section = CreditCardSection(self.driver)

        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()

        credit_card_section.credit_card()
        assert "Tarjeta" in credit_card_section.card_status().text




    def test_message_for_the_driver(self):
        self.driver.get(data.urban_routes_url)
        message = MessageForTheDriver(self.driver)

        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()

        message.write_message_to_driver()
        assert "Traiga un aperitivo" in message.message_status().get_attribute("value")




    def test_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        blanket_and_tissues = BlanketAndTissues(self.driver)

        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()

        blanket_and_tissues.switch_on()
        assert blanket_and_tissues.get_blanket_and_handkerchiefs_option_checked() is True





    def test_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        ice_creams = OrderTwoIceCreams(self.driver)

        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()

        ice_creams.order_ice_creams()

        units = ice_creams.get_units()
        assert units == "2", f"Se esperaban 2 helados, pero se encontraron {units}"





    def test_taxi_modal(self):
        self.driver.get(data.urban_routes_url)
        taxi = TaxiModal(self.driver)

        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()
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

        taxi.modal_to_search_taxi_appears()
        assert "Buscar automóvil" in taxi.taxi_modal().text, "No apareció el modal"




    def test_driver_modal(self):
        self.driver.get(data.urban_routes_url)
        driver = DriverModal(self.driver)

        # Repite código
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        rates_page = ComfortRate(self.driver)
        rates_page.select_comfort_taxi()
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

        driver.driver_modal_appears()
        assert "El conductor llegará en" in driver.driver_modal().text, "No apareció el modal"



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
