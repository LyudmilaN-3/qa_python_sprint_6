import allure
import pytest

from data.data import Data

from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария заказа самоката 1')
    @allure.description('По клику на кнопку "Заказать" на хедере страницы открыть форму заказа, '
                        'заполнить её валидными данными и проверить, '
                        'что появилось всплывающее окно с сообщением '
                        'об успешном создании заказа')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation_locator, phonenumber, color_locator, period, message',
        [Data.positive_test_data_customer_1]
    )
    def test_get_order_by_button_on_header_success(self, driver, firstname, lastname, address,
                                                   metrostation_locator, phonenumber, color_locator, period, message):
        order_page = OrderPage(driver)
        # Перейти на сайт
        order_page.go_to_site()
        # Кликнуть по кнопке "Заказать" на хедере
        order_page.get_customer_page_by_button_on_header()
        # Перейти на страницу "Для кого самокат" и заполнить поля
        order_page.fill_customer_page(firstname, lastname, address, metrostation_locator, phonenumber)
        order_page.get_rent_page()
        # Перейти на страницу "Про аренду" и заполнить поля
        order_page.fill_rent_page(color_locator, period, message)
        # Перейти к всплывающему окну "Хотите оформить заказ?" и кликнуть по кнопке "Да"
        order_page.get_order_question_page()
        # Перейти к всплывающему окну "Заказ оформлен" и получить название окна
        text = order_page.get_order_made_page().text
        assert 'Заказ оформлен' in text

    @allure.title('Проверка позитивного сценария заказа самоката 2')
    @allure.description('По клику на кнопку "Заказать" на странице открыть форму заказа, '
                        'заполнить её валидными данными и проверить, '
                        'что появилось всплывающее окно с сообщением '
                        'об успешном создании заказа')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation_locator, phonenumber, color_locator, period, message',
        [Data.positive_test_data_customer_2]
    )
    def test_get_order_by_button_on_body_success(self, driver, firstname, lastname, address,
                                                 metrostation_locator, phonenumber, color_locator, period, message):
        order_page = OrderPage(driver)
        # Перейти на сайт
        order_page.go_to_site()
        # Кликнуть по кнопке "Заказать" на странице
        order_page.get_customer_page_by_button_on_body()
        # Перейти на страницу "Для кого самокат" и заполнить поля
        order_page.fill_customer_page(firstname, lastname, address, metrostation_locator, phonenumber)
        order_page.get_rent_page()
        # Перейти на страницу "Про аренду" и заполнить поля
        order_page.fill_rent_page(color_locator, period, message)
        # Перейти к всплывающему окну "Хотите оформить заказ?" и кликнуть по кнопке "Да"
        order_page.get_order_question_page()
        # Перейти к всплывающему окну "Заказ оформлен" и получить название окна
        text = order_page.get_order_made_page().text
        assert 'Заказ оформлен' in text
