import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import Constant


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Открыть главную страницу "Самоката" '
                 f'{Constant.MAIN_URL}')
    def go_to_site(self):
        return self.driver.get(Constant.MAIN_URL)

    def find_element_by_locator(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}')

    def find_element_by_locator_and_click(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}').click()

    def scroll_to_element(self, locator, time=10):
        element = self.find_element_by_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.element_to_be_clickable(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}')

    def find_element_by_locator_and_send_keys(self, locator, value, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}').send_keys(value)

    @allure.step('Получить текущий url')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Переключить драйвер на новое окно')
    def switch_to_new_window(self, locator, value, time=30):
        original_window = self.driver.current_window_handle
        self.find_element_by_locator_and_click(locator)
        WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        return WebDriverWait(self.driver, 60).until(EC.url_contains(value))
