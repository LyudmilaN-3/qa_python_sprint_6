import allure

from locators.questions_page_locators import QuestionsPageLocator
from pages.base_page import BasePage


class QuestionsPage(BasePage):

    @allure.step('Проскроллить до блока "Вопросы о важном"')
    def get_questions_field(self):
        self.scroll_to_element(QuestionsPageLocator.BUTTON_OF_QUESTION_8)
        self.find_element_by_locator(QuestionsPageLocator.BUTTON_OF_QUESTION_8, time=40)

    @allure.step('Получить текст ответа под вопросом')
    def get_text_under_button(self, button_of_question, text_field):
        self.find_element_by_locator_and_click(button_of_question, time=30)
        text_under_button = self.find_element_by_locator(text_field, time=30).text
        return text_under_button
