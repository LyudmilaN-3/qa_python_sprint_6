from selenium.webdriver.common.by import By


class OrderPageLocator:
    ORDER_BUTTON_ON_HEADER = [
        By.XPATH, "//div[@class='Header_Header__214zg']/div/button[@class='Button_Button__ra12g']"
    ]  # Кнопка "Заказать" на хедере
    ORDER_BUTTON_ON_BODY = [
        By.XPATH, "//div[@class ='Home_ThirdPart__LSTEE'] /div/div/button"
    ]  # Кнопка "Заказать" на странице

    # Локаторы к странице "Для кого самокат"
    FIRSTNAME_INPUT_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]  # Поле для ввода имени
    LASTNAME_INPUT_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]  # Поле для ввода фамилии
    ADDRESS_INPUT_FIELD = [
        By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]  # Поле для ввода адреса
    METRO_SEARCH_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]  # Поле для выбора станции метро
    METRO_LINK_1 = [
        By.XPATH,
        "//div[@class='select-search__select']/ul/li/button/div[@class='Order_Text__2broi' and contains(text(), 'Сокольники')]"
    ]  # Ссылка для выбора станции метро "Сокольники"
    METRO_LINK_2 = [
        By.XPATH,
        "//div[@class='select-search__select']/ul/li/button/div[@class='Order_Text__2broi' and contains(text(), 'Черкизовская')]"
    ]  # Ссылка для выбора станции метро "Черкизовская"
    PHONE_NUMBER_INPUT_FIELD = [
        By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]  # Поле для ввода номера телефона
    BUTTON_THEN = [By.XPATH, "//button[contains(text(),'Далее')]"]  # Кнопка "Далее"

    # Локаторы к странице "Про аренду"
    DATE_SEARCH_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"]  # Поле для выбора даты
    TODAY_BUTTON = [By.XPATH, "//div[contains(@class, 'day--today')]"]  # Кнопка для выбора сегодняшней даты
    PERIOD_SEARCH_FIELD = [By.CSS_SELECTOR, "div[class='Dropdown-root']"]  # Поле для выбора срока аренды
    ONE_DAY_PERIOD_LINK = [
        By.XPATH, "//div[@class='Dropdown-menu']/div[contains(text(), 'сутки')]"
    ]  # Ссылка для выбора срока аренды в одни сутки
    TWO_DAYS_PERIOD_LINK = [
        By.XPATH, "//div[@class='Dropdown-menu']/div[contains(text(), 'двое суток')]"
    ]  # Ссылка для выбора срока аренды в двое суток
    CHECK_BOX_COLOR_BLACK = [
        By.CSS_SELECTOR, "div[class='Order_Checkboxes__3lWSI'] input[id='black']"
    ]  # Чек-бокс выбора цвета самоката "черный жемчуг"
    CHECK_BOX_COLOR_GREY = [
        By.CSS_SELECTOR, "div[class='Order_Checkboxes__3lWSI'] input[id='grey']"
    ]  # Чек-бокс выбора цвета самоката "серая безысходность"
    MESSAGE_INPUT_FIELD = [
        By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']"]  # Поле для ввода комментария для курьера
    ORDER_BUTTON_ON_RENT_PAGE = [
        By.XPATH, "//div[@class ='Order_Buttons__1xGrp']/button[contains(text(), 'Заказать')]"
    ]  # Кнопка "Заказать" на странице "Про аренду"
    # Локаторы к всплывающему окну "Хотите оформить заказ?"
    YES_BUTTON_ON_WINDOW = [
        By.XPATH,
        "//div[@class='Order_Modal__YZ-d3']/div[@class='Order_Buttons__1xGrp']/button[contains(text(), 'Да')]"
    ]  # Кнопка "Да" в окне

    # Локаторы к всплывающему окну "Заказ оформлен"
    TITLE_OF_WINDOW_GOT_ORDER = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']/div[@class='Order_ModalHeader__3FDaJ']"]
