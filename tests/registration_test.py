""""Тест страницы создания нового аккаунта"""

from pages.yandex_page import YandexPage


def test_registration(driver):
    """Работает ли переход на страницу и есть ли кнопка регистрации?"""
    page = YandexPage(driver)

    page.go_to_site()
    page.click_reg()
    page.click_reg_for_me_button()

    reg_button = page.check_reg_phone_is_here()
    assert reg_button == True

    print("\nКнопка создания ID работает")
