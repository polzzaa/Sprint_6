from selenium.webdriver.common.by import By

class MainPageLocators:   #Главная страница
    accept_coockie = [By.ID, "rcc-confirm-button"] #Кнопка принять куки
    yandex_button = [By.XPATH, "//img[@alt = 'Yandex']"] #Кнопка Яндекс
    scooter_button = [By.XPATH, "//img[@alt = 'Scooter']"]  #Кнопка Самокат
    order_button_header = [By.CLASS_NAME, "Button_Button__ra12g"]  # Кнопка Заказать в хэдере
    order_button_down = [By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text()='Заказать']"]  # Кнопка Заказать нижняя


    question_button_1 = [By.ID, "accordion__heading-0"] #Вопрос 1: Сколько это стоит? И как оплатить?
    question_button_2 = [By.ID, "accordion__heading-1"] #Вопрос 2: Хочу сразу несколько самокатов! Так можно?
    question_button_3 = [By.ID, "accordion__heading-2"] #Вопрос 3: Как рассчитывается время аренды?
    question_button_4 = [By.ID, "accordion__heading-3"] #Вопрос 4: Можно ли заказать самокат прямо на сегодня?
    question_button_5 = [By.ID, "accordion__heading-4"] #Вопрос 5: Можно ли продлить заказ или вернуть самокат раньше?
    question_button_6 = [By.ID, "accordion__heading-5"] #Вопрос 6: Вы привозите зарядку вместе с самокатом?
    question_button_7 = [By.ID, "accordion__heading-6"] #Вопрос 7: Можно ли отменить заказ?
    question_button_8 = [By.ID, "accordion__heading-7"] #Вопрос 8: Я жизу за МКАДом, привезёте?

    answer_1 = [By.ID, "accordion__panel-0"] #Ответ на вопрос 1
    answer_2 = [By.ID, "accordion__panel-1"] #Ответ на вопрос 2
    answer_3 = [By.ID, "accordion__panel-2"] #Ответ на вопрос 3
    answer_4 = [By.ID, "accordion__panel-3"] #Ответ на вопрос 4
    answer_5 = [By.ID, "accordion__panel-4"] #Ответ на вопрос 5
    answer_6 = [By.ID, "accordion__panel-5"] #Ответ на вопрос 6
    answer_7 = [By.ID, "accordion__panel-6"] #Ответ на вопрос 7
    answer_8 = [By.ID, "accordion__panel-7"] #Ответ на вопрос 8









