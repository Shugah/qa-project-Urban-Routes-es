from base_test import BaseTest
from LandingPageMethods import (
    UrbanRoutesPage,
    ComfortRate,
    PhoneNumberSection,
    CreditCardSection,
    MessageForTheDriver,
    BlanketAndTissues,
    OrderTwoIceCreams,
    TaxiModal,
    DriverModal
)
import data





class TestUrbanRoutes(BaseTest):

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)

        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to




    def test_comfort_rate(self):
        rates_page = ComfortRate(self.driver)

        comfort_rate_status = rates_page.comfort_status()
        assert "active" in comfort_rate_status.get_attribute("class")




    def test_phone_number(self):

        phone_section = PhoneNumberSection(self.driver)

        phone_section.phone_number()
        assert "+1" in phone_section.phone_status().text




    def test_credit_card(self):
        credit_card_section = CreditCardSection(self.driver)

        credit_card_section.credit_card()
        assert "Tarjeta" in credit_card_section.card_status().text




    def test_message_for_the_driver(self):
        message = MessageForTheDriver(self.driver)

        message.write_message_to_driver()
        assert "Traiga un aperitivo" in message.message_status().get_attribute("value")




    def test_blanket_and_tissues(self):
        blanket_and_tissues = BlanketAndTissues(self.driver)

        blanket_and_tissues.switch_on()
        assert blanket_and_tissues.get_blanket_and_handkerchiefs_option_checked() is True





    def test_ice_creams(self):
        ice_creams = OrderTwoIceCreams(self.driver)

        ice_creams.order_ice_creams()
        assert ice_creams.get_units() == "2"






    def test_taxi_modal(self):
        self.prepare_full_order() #repite proceso
        taxi = TaxiModal(self.driver)

        assert "Buscar automóvil" in taxi.taxi_modal().text, "No apareció el modal"




    def test_driver_modal(self):
        self.prepare_full_order()  #repite proceso
        driver = DriverModal(self.driver)
        driver.driver_modal_appears()

        assert "El conductor llegará en" in driver.driver_modal().text, "No apareció el modal"



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
