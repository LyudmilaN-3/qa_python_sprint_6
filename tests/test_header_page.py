import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import Constant

from pages.header_page import HeaderPage


class TestHeaderPage:

    @allure.title('Проверка перехода на главную страницу по клику на лого Самокат на хедере')
    @allure.description('Проверить переход на главную страницу Самоката '
                        'по клику на лого "Самокат" на хедере страницы')
    def test_get_main_page_by_logo_scooter_on_header_success(self, driver):
        header_page = HeaderPage(driver)
        # Перейти на сайт
        header_page.go_to_site()
        # Перейти на главную страницу по клику на лого Самокат на хедере
        header_page.get_main_page_by_logo_scooter_on_header()
        assert driver.current_url == Constant.MAIN_URL

    @allure.title('Проверка перехода на главную страницу Дзена по клику на лого Яндекс на хедере')
    @allure.description('Проверить переход на главную страницу Дзена '
                        'по клику на лого "Яндекс" на хедере страницы')
    def test_get_dzen_page_by_logo_yandex_on_header_success(self, driver):
        header_page = HeaderPage(driver)
        # Перейти на сайт
        header_page.go_to_site()
        original_window = driver.current_window_handle
        # Перейти на главную страницу Дзена по клику на лого Яндекс на хедере
        header_page.get_dzen_page_by_logo_yandex_on_header()
        WebDriverWait(driver, 30).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        assert WebDriverWait(driver, 10).until(EC.url_contains(Constant.DZEN_URL_VIA_REDIRECT))
