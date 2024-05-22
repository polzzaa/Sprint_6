from selenium.webdriver.common.by import By

class OrderPageLocators: #Страница заказа
    order_button_header = [By.CLASS_NAME, "Button_Button__ra12g"] #Кнопка Заказать в хэдере
    name_field = [By.XPATH, "//input[@placeholder = '* Имя']"] #Поле "Имя"
    last_name_field = [By.XPATH, "//input[@placeholder = '* Фамилия']"] #Поле "Фамилия"
    adress_field = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"] #Поле "Адрес: куда привезти заказ"
    station_select = [By.CLASS_NAME, "select-search__input"] #Поле "Станция метро"
    sokolniki_station = [By.XPATH, "//div[text()='Сокольники']"] #Станция метро Сокольники в выпадающем списке
    phone_field = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"] #Поле "Телефон: на него позвонит курьер"
    next_button = [By.XPATH, "//button[text()='Далее']"] #Кнопка Далее
    date_field = [By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]"] #Поле "Когда привезти самокат"
    selected_delivery_day = [By.XPATH, "//div[contains(@class, 'day--selected')]"] #Выбранный день аренды
    rental_period_field = [By.XPATH, "//div[text()='* Срок аренды']"] #Поле "Срок аренды"
    selected_rent_day = [By.XPATH, "//div[text()='сутки']"] #Сутки в выпадающем списке
    selected_black_color = [By.ID, "black"] #Черный цвет самоката
    comment_field = [By.XPATH, "//input[contains(@placeholder, 'Комментарий')]"] #Поле "Комментарий для курьера"
    order_button = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"] #Кнопка Заказать внизу
    popup_yes_button = [By.XPATH, "//button[text()= 'Да']"] #Кнопка Да во всплывающем окне
    popup_order_status = [By.XPATH, "//div[text()='Заказ оформлен']"] #Подтверждение оформления заказа










