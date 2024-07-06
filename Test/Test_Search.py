import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Page_search import SearchPage



@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    # driver.quit()

def test_search(driver):
    search_page = SearchPage(driver)
    search_page.open()  # Ensure open method is called here
    search_page.expand()
    search_page.fill_name_search_field('John')
    search_page.fill_birth_date_field("1963-12-18")
    search_page.fill_credit_field('King')
    search_page.search_locator_button()

