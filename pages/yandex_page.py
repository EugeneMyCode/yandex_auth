""""Класс для работы с главной страницой Yandex"""

import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class YandexPage(BasePage):
    """"Модель страницы авторизации Yandex"""

    PHONE_TAB = (By.CSS_SELECTOR, "button[data-type='phone']")
    PHONE_INPUT = (By.CSS_SELECTOR, "#passp-field-phone")
    SIGN_IN = (By.ID, "passp:sign-in")
    CODE_INPUT = (By.CSS_SELECTOR, "#passp-field-phoneCode")
    EMAIL_TAB = (By.CSS_SELECTOR, "button[data-type='login']")
    EMAIL_OR_LOGIN_INPUT = (By.CSS_SELECTOR, "#passp-field-login")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#passp-field-passwd")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, "#password-toggle")
    WRONG_PASSWORD_ERROR = (By.ID, "field:input-passwd:hint")
    VK_BUTTON = (By.CSS_SELECTOR, ".PasspIcon.PasspIcon_vk.PasspIcon_size_s")
    VK_LOGIN = (By.NAME, "login")
    REG = (By.ID, "passp:exp-register")
    REG_FOR_ME = (By.CSS_SELECTOR, "li:nth-child(1) button:nth-child(1)")
    REG_PHONE = (By.CSS_SELECTOR, "#passp-field-phone")

    url = f'{os.getenv("URL")}'

    def click_phone_tab_button(self):
        """"Клик по табу с вводом номера телефона"""
        self.find_element(self.PHONE_TAB).click()

    def clear_phone_input(self):
        """"Очистка поля ввода номера телефона"""
        self.find_element(self.PHONE_INPUT).clear()

    def send_phone_number(self):
        """"Ввод номера телефона в соответствующее поле"""
        self.find_element(self.PHONE_INPUT).send_keys(f'{os.getenv("PHONE")}')

    def click_sign_in_button(self):
        """"Клик по кнопке 'Войти'"""
        self.find_element(self.SIGN_IN).click()

    def check_code_input_is_here(self):
        """"Проверка доступа поля для ввода кода"""
        return self.find_element(self.CODE_INPUT).is_enabled()
    
    def click_email_tab_button(self):
        """"Клик по табу email"""
        self.find_element(self.EMAIL_TAB).click()

    def send_email_address(self):
        """"Ввод email в соответствующее поле"""
        self.find_element(self.EMAIL_OR_LOGIN_INPUT).send_keys(f'{os.getenv("EMAIL")}')

    def send_login(self):
        """"Ввод логин в соответствующее поле"""
        self.find_element(self.EMAIL_OR_LOGIN_INPUT).send_keys(f'{os.getenv("LOGIN")}')

    def check_password_input_is_here(self):
        """"Проверка доступа поля для ввода пароля"""
        return self.find_element(self.PASSWORD_INPUT).is_enabled()
    
    def send_password(self):
        """"Ввод пароля в соответствующее поле"""
        self.find_element(self.PASSWORD_INPUT).send_keys(f'{os.getenv("PASSWORD")}')

    def check_password_error_is_here(self):
        """"Проверка ошибки при авторизации с несуществующего аккаунта"""
        return self.find_element(self.WRONG_PASSWORD_ERROR).is_enabled()
    
    def click_vk_button(self):
        """"Клик по кнопке логина через ВК"""
        self.find_element(self.VK_BUTTON).click()

    def check_vk_login_field_is_here(self):
        """"Проверка доступа поля в новом окне для ввода логина ВК"""
        return self.find_element(self.VK_LOGIN).is_enabled()
    
    def click_reg(self):
        """"Клик по кнопке 'Создать ID'"""
        self.find_element(self.REG).click()

    def click_reg_for_me_button(self):
        """"Клик по всплывающей кнопке 'Для себя'"""
        self.find_element(self.REG_FOR_ME).click()

    def check_reg_phone_is_here(self):
        """"Проверка доступа ввода телефона для регистрации"""
        return self.find_element(self.REG_PHONE).is_enabled()
