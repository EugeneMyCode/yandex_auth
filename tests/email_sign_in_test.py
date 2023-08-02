""""Тест входа по email"""

from pages.yandex_page import YandexPage


def test_email_sign_in(driver):
    """Поле ввода кода из почты находится на странице?"""
    page = YandexPage(driver)

    page.go_to_site()
    page.click_email_tab_button()
    page.send_email_address()
    page.click_sign_in_button()

    status = page.check_code_input_is_here()
    assert status == True
