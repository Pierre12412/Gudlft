import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver


@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass
class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):
        self.driver.get(url='http://127.0.0.1:5000')
        self.driver.maximize_window()
        assert "Welcome to the GUDLFT Registration Portal!" in self.driver.find_element(By.TAG_NAME, 'h1').text

    def test_connect_allowed(self):
        # Login
        email = "admin@irontemple.com"
        email_text_field = self.driver.find_element(By.NAME,'email')
        button = self.driver.find_element(By.XPATH,'/html/body/form/button')
        email_text_field.send_keys(email)
        button.click()

    # Do the same things as a normal person
    def test_book_places(self):
        button = self.driver.find_element(By.LINK_TEXT,'Book Places')
        button.click()
        form = self.driver.find_element(By.NAME,'places')
        form.send_keys(Keys.CONTROL + "a")
        form.send_keys(Keys.DELETE)
        book_button = self.driver.find_element(By.XPATH, '/html/body/form/button')

        # Try a too low number
        form.send_keys(2)
        book_button.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/book/Fall%20Classic/Iron%20Temple'

        # Try a number which is not multiple of 3
        form.send_keys(Keys.CONTROL + "a")
        form.send_keys(Keys.DELETE)
        form.send_keys(4)
        book_button.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/book/Fall%20Classic/Iron%20Temple'

        # Try a too large number
        form.send_keys(Keys.CONTROL + "a")
        form.send_keys(Keys.DELETE)
        form.send_keys(10)
        book_button.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/book/Fall%20Classic/Iron%20Temple'

        # Try the good number
        form.send_keys(Keys.CONTROL + "a")
        form.send_keys(Keys.DELETE)
        form.send_keys(3)
        book_button.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/purchasePlaces'
        assert 'Great-booking complete!' in self.driver.find_element(By.XPATH,'/html/body/ul[1]/li').text
        assert '1' in self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]').text

        # Logout
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()