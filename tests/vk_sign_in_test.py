""""Тест входа через ВК"""

from pages.yandex_page import YandexPage


def test_vk_sign_in(driver):
    """Открывается новое окно для авторизации через ВК?"""
    page = YandexPage(driver)

    page.go_to_site()
    page.click_vk_button()
    page.go_to_opened_window()

    # Проверка нового окна, что это переход на ВК
    new_window_is_vk = page.current_url().startswith('https://id.vk.com/')
    assert new_window_is_vk == True

    # Проверка наличия поля для ввода логина/почты в ВК
    vk_login_field = page.check_vk_login_field_is_here()
    assert vk_login_field == True

    print("\nАвторизация через vk работает")
