from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart_button = "//div[@id='shopping_cart_container']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Click select product 1")

    def click_select_product_2(self):
        self.get_product_2().click()
        print("Click select product 2")

    def click_select_product_3(self):
        self.get_product_3().click()
        print("Click select product 3")

    def click_cart(self):
        self.get_cart_button().click()
        print("Click cart")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click menu button")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click link about")

    # Methods

    def add_to_cart_product_1(self):
        Logger.add_start_step(method="add_to_cart_product_1")
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_product_1")

    def add_to_cart_product_2(self):
        Logger.add_start_step(method="add_to_cart_product_2")
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_product_2")

    def add_to_cart_product_3(self):
        Logger.add_start_step(method="add_to_cart_product_3")
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_product_3")

    def select_menu_about(self):
        Logger.add_start_step(method="select_menu_about")
        self.get_current_url()
        self.click_menu_button()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')
        Logger.add_end_step(url=self.driver.current_url, method="select_menu_about")
