import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about():  # авторизация и переход на страницу about
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    r = requests.get(
        'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
    rjson = json.loads(r.text)
    version = rjson['channels']['Stable']['version']
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager(version).install()))

    print("Start test")

    login = LoginPage(driver)
    login.authorisation()
    mp = MainPage(driver)
    mp.select_menu_about()
    mp.assert_url('https://saucelabs.com/')
    driver.close()
