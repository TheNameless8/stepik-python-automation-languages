import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_product_page_have_add_button(browser):
    browser.get(link)
    time.sleep(10)
    basket_button_count = browser.find_elements_by_class_name("btn-add-to-basket")
    #assert basket_button, "Should be a button"
    assert len(basket_button_count) == 1, "Нет кнопки добавления в корзину"


