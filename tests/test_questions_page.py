import allure
import pytest

from data.data import Data
from pages.questions_page import QuestionsPage


class TestQuestionsPage:

    test_data_for_questions_page = list(zip(Data.buttons_of_question, Data.text_fields, Data.texts_of_answer))

    @allure.title('Проверка соответствия текста ответа вопросу в разделе "Вопросы о важном"')
    @allure.description('На странице найти элемент с вопросом, '
                        'раскрыть выпадающий список с ответом и '
                        'сверить соответствие ответа вопросу')
    @pytest.mark.parametrize('button_of_question, text_field, text_of_answer', test_data_for_questions_page)
    def test_click_by_button_open_text_success(self, driver, button_of_question, text_field, text_of_answer):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site()
        questions_page.get_questions_field()
        text = questions_page.get_text_under_button(button_of_question, text_field)
        assert text == text_of_answer
