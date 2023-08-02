""""Базовый класс с методами для работы на страницах"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """"Модель страницы"""

    def __init__(self, driver):
        """"Инициализация вебдрайвера и часто используемых классов вебдрайвера"""
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 20)

    def find_element(self, locator):
        """"Поиск элемента по локатору"""
        return self._wait.until(EC.presence_of_element_located(locator), message='Элемент не найден')

    def go_to_site(self):
        """"Переход на сайт из класса потомка"""
        return self.driver.get(self.url)

    def go_to_opened_window(self):
        """"Переключение на второе окно браузера"""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def current_url(self):
        """"Возвращает текущий url"""
        return self.driver.current_url
        
