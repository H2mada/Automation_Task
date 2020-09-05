from page import Page
import requests

def test_case_3 (browser):
    page = Page(browser)
    
    #  Navigate to the URL https://www.sogeti.com/
    page.load()

    #  Click the Worldwide Dropdown link in Page Header.
    page.click('//*[@id="header"]/div[1]/div[2]/div[2]/div[2]')

    #  A Country dropdown list is displayed.
    assert True == page.is_displayed('//*[@id="header"]/div[3]')

    #  Assert that all the Country specific Sogeti links are working. 
    for link in page.get_links('//*[@id="header"]/div[3]'):
        assert 200 == requests.head(link.get_attribute('href')).status_code