""""Тест страницы создания нового аккаунта"""

from pages.yandex_page import YandexPage


def test_registration(driver):
    """Работает ли переход на страницу и есть ли кнопка регистрации?"""
    page = YandexPage(driver)

    page.go_to_site()
    page.click_reg()
    page.click_reg_for_me_button()

    # После перехода мы попадаем на старницу регистрации
    reg_url = page.current_url().startswith('https://passport.yandex.ru/registration')
    assert reg_url == True

    # Кнопка регистрации, которую нажимаем после заполнения всех полей
    reg_button = page.check_reg_button_is_here()
    assert reg_button == True
