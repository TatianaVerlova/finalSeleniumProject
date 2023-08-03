import json
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):  # авторизация и добавление в корзину продукта 1
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    r = requests.get(
        'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
    rjson = json.loads(r.text)
    version = rjson['channels']['Stable']['version']
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager(version).install()))

    print("Start test 1")

    login = LoginPage(driver)
    login.authorisation()
    mp = MainPage(driver)
    mp.add_to_cart_product_1()
    cp = CartPage(driver)
    cp.product_conformation()
    print("Finish test 1")
    driver.close()

@pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):  # авторизация и добавление в корзину продукта 2
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    r = requests.get(
        'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
    rjson = json.loads(r.text)
    version = rjson['channels']['Stable']['version']
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager(version).install()))

    print("Start test 2")

    login = LoginPage(driver)
    login.authorisation()
    mp = MainPage(driver)
    mp.add_to_cart_product_2()
    cp = CartPage(driver)
    cp.product_conformation()
    print("Finish test 2")
    driver.close()

@pytest.mark.run(order=2)
def test_buy_product_3():  # авторизация и добавление в корзину продукта 3
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    r = requests.get(
        'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
    rjson = json.loads(r.text)
    version = rjson['channels']['Stable']['version']
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager(version).install()))

    print("Start test 3")

    login = LoginPage(driver)
    login.authorisation()
    mp = MainPage(driver)
    mp.add_to_cart_product_3()
    cp = CartPage(driver)
    cp.product_conformation()
    print("Finish test 3")
    driver.close()
