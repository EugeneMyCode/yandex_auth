""""Тест входа по логину"""

from pages.yandex_page import YandexPage


def test_login_sign_in(driver):
    """Поле ввода пароля находится на странице?"""
    page = YandexPage(driver)

    page.go_to_site()
    page.click_email_tab_button()
    page.send_login()
    page.click_sign_in_button()

    status = page.check_password_input_is_here()
    assert status == True

    page.send_password()
    page.click_sign_in_button()
    
    # Доп. проверка, что аккаунта с таким логином/паролем не существует
    error = page.check_password_error_is_here()
    assert error == True

    print("\nСтраница входа работает и нельзя войти под несуществующим аккаунтом")
