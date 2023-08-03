import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_buy_product(set_up):  # авторизация и покупка
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    r = requests.get(
        'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
    rjson = json.loads(r.text)
    version = rjson['channels']['Stable']['version']
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager(version).install()))

    login = LoginPage(driver)
    login.authorisation()
    mp = MainPage(driver)
    mp.add_to_cart_product_1()
    cp = CartPage(driver)
    cp.product_conformation()
    cip = ClientInfoPage(driver)
    cip.input_client_info()
    pp = PaymentPage(driver)
    pp.payment()
    fp = FinishPage(driver)
    fp.finish()
    driver.close()
