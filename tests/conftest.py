
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# ----------------------------------------------------------------------
# Fixture: Create the WebDriver instance
# ----------------------------------------------------------------------

@pytest.fixture
def browser():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
