from selenium.webdriver.common.by import By


class QuestionsPageLocator:
    BUTTON_OF_QUESTION_1 = [By.ID, "accordion__heading-0"]
    BUTTON_OF_QUESTION_2 = [By.ID, "accordion__heading-1"]
    BUTTON_OF_QUESTION_3 = [By.ID, "accordion__heading-2"]
    BUTTON_OF_QUESTION_4 = [By.ID, "accordion__heading-3"]
    BUTTON_OF_QUESTION_5 = [By.ID, "accordion__heading-4"]
    BUTTON_OF_QUESTION_6 = [By.ID, "accordion__heading-5"]
    BUTTON_OF_QUESTION_7 = [By.ID, "accordion__heading-6"]
    BUTTON_OF_QUESTION_8 = [By.ID, "accordion__heading-7"]
    TEXT_FIELD_1 = [By.XPATH, "//div[@id='accordion__panel-0']/p"]
    TEXT_FIELD_2 = [By.XPATH, "//div[@id='accordion__panel-1']/p"]
    TEXT_FIELD_3 = [By.XPATH, "//div[@id='accordion__panel-2']/p"]
    TEXT_FIELD_4 = [By.XPATH, "//div[@id='accordion__panel-3']/p"]
    TEXT_FIELD_5 = [By.XPATH, "//div[@id='accordion__panel-4']/p"]
    TEXT_FIELD_6 = [By.XPATH, "//div[@id='accordion__panel-5']/p"]
    TEXT_FIELD_7 = [By.XPATH, "//div[@id='accordion__panel-6']/p"]
    TEXT_FIELD_8 = [By.XPATH, "//div[@id='accordion__panel-7']/p"]
