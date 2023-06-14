# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

"""
Код выполняет ряд операций по списку:
Авторизоваться на сайте https://fix-online.sbis.ru/
Перейти в реестр Контакты
Отправить сообщение самому себе
Убедиться, что сообщение появилось в реестре
Удалить это сообщение и убедиться, что удалили
"""

login = 'Николаев_неСтенд'
password = 'Николаев_неСтенд123'

driver = webdriver.Chrome()
sbis_site = 'https://test-online.sbis.ru/'
driver.get(sbis_site)
try:
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.NAME, 'Login').send_keys(login)
    driver.find_element(By.XPATH, '//span[@data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]').click()
    driver.find_element(By.NAME, 'Password').send_keys(password)
    driver.find_element(By.XPATH, '//span[@data-qa="auth-AdaptiveLoginForm__signInButton"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//span[@data-qa="NavigationPanels-Accordion__title"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@href="/page/dialogs"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[@data-qa="sabyPage-addButton"]').click()
    time.sleep(2)
    date = datetime.date.today()
    driver.find_element(By.XPATH, f'//input[@name="ws-input_{date}"]').send_keys('Николаев_неСтенд')
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[@title="Николаев_неСтенд Иван"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@data-qa="textEditor_slate_Field"]').send_keys('Текстовое сообщение')
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[@data-qa="msg-send-editor__send-button"]'
                                  '/span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled '
                                  'controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center '
                                  'controls-Button__wrapper_filled_l"]').click()
    time.sleep(2)
    if driver.find_element(By.XPATH, '//div[@class="msg-entity-text msg-entity_font_croppless '
                                     'richEditor_richContentRender_fontSize-m_theme-default '
                                     'controls_RichEditor_theme-default richEditor_richContentRender_theme-default '
                                     'richEditor_richContentRender richEditor_richContentRender_lineHeight-s '
                                     'richEditor_richContentRender_colorPalette-first '
                                     'richEditor_richContentRender_readOnly msg-dialogs-item__message-text '
                                     'msg-entity-text_normalized controls-List_DragNDrop__notDraggable '
                                     'ws-flex-shrink-1 msg-entity-expander__content '
                                     'ws-flex-grow-1 ws-flex-shrink-1"]').text == 'Текстовое сообщение':
        driver.find_element(By.XPATH, '//div[@class="msg-entity-text msg-entity_font_croppless '
                                      'richEditor_richContentRender_fontSize-m_theme-default '
                                      'controls_RichEditor_theme-default '
                                      'richEditor_richContentRender_theme-default '
                                      'richEditor_richContentRender '
                                      'richEditor_richContentRender_lineHeight-s '
                                      'richEditor_richContentRender_colorPalette-first '
                                      'richEditor_richContentRender_readOnly msg-dialogs-item__message-text '
                                      'msg-entity-text_normalized controls-List_DragNDrop__notDraggable '
                                      'ws-flex-shrink-1 msg-entity-expander__content '
                                      'ws-flex-grow-1 ws-flex-shrink-1"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[@data-qa="remove"]').click()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, '//div[@class="msg-entity-text msg-entity_font_croppless '
                                         'richEditor_richContentRender_fontSize-m_theme-default '
                                         'controls_RichEditor_theme-default '
                                         'richEditor_richContentRender_theme-default '
                                         'richEditor_richContentRender '
                                         'richEditor_richContentRender_lineHeight-s '
                                         'richEditor_richContentRender_colorPalette-first '
                                         'richEditor_richContentRender_readOnly msg-dialogs-item__message-text '
                                         'msg-entity-text_normalized controls-List_DragNDrop__notDraggable '
                                         'ws-flex-shrink-1 msg-entity-expander__content '
                                         'ws-flex-grow-1 ws-flex-shrink-1"]').text == 'Тестовое сообщение'
        except NoSuchElementException:
            driver.execute_script('alert(arguments[0])', 'Сообщение удалено')
            time.sleep(2)
finally:
    driver.close()