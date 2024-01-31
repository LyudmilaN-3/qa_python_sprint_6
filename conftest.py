import allure
import pytest
from selenium import webdriver


@allure.title('Подготовка драйвера Firefox и его выключение')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
