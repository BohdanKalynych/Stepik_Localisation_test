from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_different_localisations(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element(By.XPATH,
                                                "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert add_to_basket_button.is_displayed(), "element is not visible on the page"
