import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.imdb.com/search/name/'
        self.expand_field_locator = (By.XPATH,
                                     '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')
        self.name_field_locator = (By.NAME, 'name-text-input')
        self.birth_date_field_locator = (By.NAME, 'Enter birth date from')
        self.death_date_field_locator = (By.NAME, 'death_date')
        self.gender_field_locator = (By.XPATH,
                                     '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[2]/div/section')
        self.topic_sort_by_dropdown_locator = (By.NAME, 'within-topic-dropdown')
        self.credit_field_button = (By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')
        self.awards_expand_button_locator = (By.XPATH, "//button[contains(text(), 'Awards & recognition')]")
        self.oscar_award_checkbox_locator = (By.XPATH, "//label[contains(text(), 'Oscar-Winning')]")
        self.search_button_locator = (By.XPATH, "//button[@type='submit']")
        self.search_locator = (By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button")

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("window.scrollTo(500, 500);")

    def expand(self):
        try:
            expand_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.expand_field_locator)
            )
            expand_field.click()
            print("\n Menu option expanded successfully .")
        except:
            print("\n Expand Element not found within the given time")
            # sys.exit(1)

    def fill_name_search_field(self, text):
        try:
            self.name_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.name_field_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", self.name_field)
            self.name_field.clear()
            self.name_field.send_keys(text)
            print("\n Name entered successfully.")
        except:
            print("\n Name Element not found within the given time")

    def fill_birth_date_field(self, birth_date):
        try:
            self.birth_date_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.birth_date_field_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", self.birth_date_field)
            actions = ActionChains(self.driver)
            self.birth_date_field.clear()
            self.birth_date_field.send_keys(birth_date)
            actions.send_keys(Keys.ENTER)  # Press the Enter key to select
            actions.perform()
            # self.birth_date_field.send_keys(Keys.TAB)
            print("\n Birth Date entered successfully.")
        except:
            print("\n Birth Date not found within the given time")

    def fill_credit_field(self, text):
        try:
            self.credit_field_button1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.credit_field_button))
            self.driver.execute_script("arguments[0].scrollIntoView();", self.credit_field_button1)
            actions = ActionChains(self.driver)
            self.credit_field_button1.clear()
            self.credit_field_button1.send_keys(text)
            actions.pause(2)  # Wait for suggestions to appear
            actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
            actions.pause(1)  # Pause briefly to ensure the selection
            actions.send_keys(Keys.ENTER)  # Press the Enter key to select
            actions.perform()
            print("\n Credit Search performed successfully.")
        except:
            print("\n Credit Element not found within the given time")

    def search_locator_button(self):
        try:
            self.search_locator_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.search_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", self.search_locator_button)
            self.search_locator_button.click()
        except:
            print("\n Search not located")