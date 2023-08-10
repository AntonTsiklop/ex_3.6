from selenium.webdriver.common.by import By


def test_presence_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"), 'Нет кнопки "Добавить в корзину"'
