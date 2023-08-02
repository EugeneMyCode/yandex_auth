""""Тест входа по телефону"""

from pages.yandex_page import YandexPage


def test_phone_sign_in(driver):
    """Поле ввода СМС находится на странице?"""
    page = YandexPage(driver)

    page.go_to_site()
    page.click_phone_tab_button()
    page.clear_phone_input()
    page.send_phone_number()
    page.click_sign_in_button()

    status = page.check_code_input_is_here()
    assert status == True
