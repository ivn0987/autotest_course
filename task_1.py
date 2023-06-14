# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Код выполняет ряд операций по списку: 
Перейти на https://sbis.ru/
Перейти в раздел "Контакты"
Найти баннер Тензор, кликнуть по нему
Перейти на https://tensor.ru/
Проверить, что есть блок новости "Сила в людях"
Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
"""
driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'

driver.get(sbis_site)
try:
    driver.find_element(By.XPATH, '//a[@href="/contacts"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://tensor.ru/"]').click()
    time.sleep(1)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    power_in_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    driver.execute_script('return arguments[0].scrollIntoView(true)', power_in_people)
    if power_in_people.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-title').text == 'Сила в людях':
        more = power_in_people.find_element(By.XPATH, '//p/a[@href="/about"]')
        more.click()
        time.sleep(1)
    driver.execute_script('alert(arguments[0])', f'Это точно страница {driver.current_url}')
    time.sleep(5)
finally:
    driver.close()


