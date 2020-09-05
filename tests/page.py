from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:

    # URL
    URL = 'https://www.sogeti.com/'

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title
    
    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def get_attribute_of_element(self, xpath, attribute):
        element = self.browser.find_element_by_xpath(xpath)
        return element.get_attribute(attribute)

    def hover(self, xpath):
        element_to_hover_over = self.browser.find_element_by_xpath(xpath)
        hover = ActionChains(self.browser).move_to_element(element_to_hover_over)
        hover.perform()
    
    def click(self, xpath):
        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def scroll_into_view(self, xpath):
        element = self.browser.find_element_by_xpath(xpath)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def input_to(self, xpath, value):
        element = self.browser.find_element_by_xpath(xpath)
        element.send_keys(value)
    def is_displayed(self, xpath):
        element = self.browser.find_element_by_xpath(xpath)
        if element.is_displayed:
            return True
        return False
    def get_links(self, xpath):
        element = self.browser.find_element_by_xpath(xpath)
        return element.find_elements_by_tag_name('a')
       
