from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
...

# Добавь явное ожидание для загрузки страницы
...

# Кликни по кнопке добавления нового контента
driver.find_element(...)...

# Введи название нового места
driver.find_element(...)...

# Введи ссылку на изображение
driver.find_element(...)...

# Сохрани контент
driver.find_element(...)...

# Дождись появления кнопки удаления карточки
WebDriverWait(...).until(...)

# Удали контент
driver.find_element(...)...

driver.quit()
