import allure

from locators.order_page_locators import OrderPageLocator
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Перейти на страницу "Для кого самокат" по кнопке "Заказать" на хедере')
    def get_customer_page_by_button_on_header(self):
        self.find_element_by_locator_and_click(OrderPageLocator.ORDER_BUTTON_ON_HEADER)

    @allure.step('Перейти на страницу "Для кого самокат" по кнопке "Заказать" на странице')
    def get_customer_page_by_button_on_body(self):
        self.scroll_to_element(OrderPageLocator.ORDER_BUTTON_ON_BODY)
        self.find_element_by_locator_and_click(OrderPageLocator.ORDER_BUTTON_ON_BODY)

    @allure.step('Заполнить поля страницы "Для кого самокат"')
    def fill_customer_page(self, firstname, lastname, address, metrostation_locator, phonenumber):
        self.find_element_by_locator_and_send_keys(OrderPageLocator.FIRSTNAME_INPUT_FIELD, firstname)
        self.find_element_by_locator_and_send_keys(OrderPageLocator.LASTNAME_INPUT_FIELD, lastname)
        self.find_element_by_locator_and_send_keys(OrderPageLocator.ADDRESS_INPUT_FIELD, address)
        self.find_element_by_locator_and_click(OrderPageLocator.METRO_SEARCH_FIELD)
        self.find_element_by_locator_and_click(metrostation_locator)
        self.find_element_by_locator_and_send_keys(OrderPageLocator.PHONE_NUMBER_INPUT_FIELD, phonenumber)

    @allure.step('Перейти на страницу "Про аренду"')
    def get_rent_page(self):
        self.find_element_by_locator_and_click(OrderPageLocator.BUTTON_THEN)

    @allure.step('Заполнить поля страницы "Про аренду"')
    def fill_rent_page(self, color_locator, period, message):
        self.find_element_by_locator_and_click(OrderPageLocator.DATE_SEARCH_FIELD)
        self.find_element_by_locator_and_click(OrderPageLocator.TODAY_BUTTON)
        self.find_element_by_locator_and_click(OrderPageLocator.PERIOD_SEARCH_FIELD)
        self.find_element_by_locator_and_click(period)
        self.find_element_by_locator_and_click(color_locator)
        self.find_element_by_locator_and_send_keys(OrderPageLocator.MESSAGE_INPUT_FIELD, message)

    @allure.step('Перейти к всплывающему окну "Хотите оформить заказ?"')
    def get_order_question_page(self):
        self.find_element_by_locator_and_click(OrderPageLocator.ORDER_BUTTON_ON_RENT_PAGE)

    @allure.step('Перейти к всплывающему окну "Заказ оформлен" и вернуть текст в окне')
    def get_order_made_page(self):
        self.find_element_by_locator_and_click(OrderPageLocator.YES_BUTTON_ON_WINDOW)
        return self.find_element_by_locator(OrderPageLocator.TITLE_OF_WINDOW_GOT_ORDER)
