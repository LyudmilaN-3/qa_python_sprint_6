from .constants import Constant
from locators.order_page_locators import OrderPageLocator
from locators.questions_page_locators import QuestionsPageLocator


class Data:
    # тестовые данные для test_questions_page
    buttons_of_question = [
        QuestionsPageLocator.BUTTON_OF_QUESTION_1,
        QuestionsPageLocator.BUTTON_OF_QUESTION_2,
        QuestionsPageLocator.BUTTON_OF_QUESTION_3,
        QuestionsPageLocator.BUTTON_OF_QUESTION_4,
        QuestionsPageLocator.BUTTON_OF_QUESTION_5,
        QuestionsPageLocator.BUTTON_OF_QUESTION_6,
        QuestionsPageLocator.BUTTON_OF_QUESTION_7,
        QuestionsPageLocator.BUTTON_OF_QUESTION_8,
    ]
    text_fields = [
        QuestionsPageLocator.TEXT_FIELD_1,
        QuestionsPageLocator.TEXT_FIELD_2,
        QuestionsPageLocator.TEXT_FIELD_3,
        QuestionsPageLocator.TEXT_FIELD_4,
        QuestionsPageLocator.TEXT_FIELD_5,
        QuestionsPageLocator.TEXT_FIELD_6,
        QuestionsPageLocator.TEXT_FIELD_7,
        QuestionsPageLocator.TEXT_FIELD_8,
    ]
    texts_of_answer = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. '
        'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. '
        'Мы привозим самокат 8 мая в течение дня. '
        'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. '
        'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
        'Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
    ]
    # тестовые данные для test_order_page
    positive_test_data_customer_1 = [
        Constant.TEST_FIRSTNAME_CUSTOMER_1,
        Constant.TEST_LASTNAME_CUSTOMER_1,
        Constant.TEST_ADDRESS_CUSTOMER_1,
        OrderPageLocator.METRO_LINK_1,
        Constant.TEST_PHONENUMBER_CUSTOMER_1,
        OrderPageLocator.CHECK_BOX_COLOR_BLACK,
        OrderPageLocator.ONE_DAY_PERIOD_LINK,
        Constant.TEST_MESSAGE_CUSTOMER_1
    ]
    positive_test_data_customer_2 = [
        Constant.TEST_FIRSTNAME_CUSTOMER_2,
        Constant.TEST_LASTNAME_CUSTOMER_2,
        Constant.TEST_ADDRESS_CUSTOMER_2,
        OrderPageLocator.METRO_LINK_2,
        Constant.TEST_PHONENUMBER_CUSTOMER_2,
        OrderPageLocator.CHECK_BOX_COLOR_GREY,
        OrderPageLocator.TWO_DAYS_PERIOD_LINK,
        Constant.TEST_MESSAGE_CUSTOMER_2,
    ]
