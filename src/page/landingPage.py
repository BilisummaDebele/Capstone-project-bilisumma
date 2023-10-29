from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_register(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[@class='btnSubmit'])[2]"))
            )
            assert submit_button.is_displayed(), "Submit button is not displayed on the page."
            submit_button.click()

        except Exception as e:
            print(f"Assertion failed: {e}")
