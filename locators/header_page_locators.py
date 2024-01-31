from selenium.webdriver.common.by import By


class HeaderPageLocator:
    LOGO_YANDEX = [By.CSS_SELECTOR, "div[class='Header_Logo__23yGT'] img[alt='Yandex']"]  # Логотип Яндекс
    LOGO_SCOOTER = [By.CSS_SELECTOR, "div[class='Header_Logo__23yGT'] img[alt='Scooter']"]  # Логотип Самокат
    DZEN_TITLE = [By.CSS_SELECTOR, "div[class='dzen-desktop__yandexSearchContainer-2y']"]
    CLOSE_BUTTON = [By.CSS_SELECTOR, "span[class='vaf13e206 d6c1fa8e2 scdf965da k34e928e1'] svg"]
