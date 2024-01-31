import allure

from data.constants import Constant
from locators.header_page_locators import HeaderPageLocator
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Перейти на главную страницу "Самоката" по клику на лого "Самокат"')
    def get_main_page_by_logo_scooter_on_header(self):
        self.find_element_by_locator_and_click(HeaderPageLocator.LOGO_SCOOTER)

    @allure.step('Перейти редиректом на главную страницу Дзена по клику на лого Яндекса')
    def get_dzen_page_by_logo_yandex_on_header(self):
        self.switch_to_new_window(HeaderPageLocator.LOGO_YANDEX, Constant.DZEN_URL_VIA_REDIRECT)
