
from page import Page

def test_case_1 (browser):
    
    page = Page(browser)

    # Navigate to the URL https://www.sogeti.com/
    page.load()

    # Hover over Services Link
    page.hover('//*[@id="header"]/div[1]/nav/ul/li[3]/div')

    #  and then Click Automation link.
    page.click('//*[@id="header"]/div[1]/div[5]/ul/li[7]/a')

    # Verify that Automation Screen is displayed
    assert 'Automation' in page.title()

    # and “Automation” text is visible in Page
    assert 'Automation' in page.get_attribute_of_element('//*[@id="primary_content"]/div/div[2]/div/h1/span','textContent')

    # Hover again over Services Link
    page.hover('//*[@id="header"]/div[1]/nav/ul/li[3]/div')

    # Verify that the Services and Automation are selected
    assert 'selected' in page.get_attribute_of_element('//*[@id="header"]/div[1]/div[5]/ul/li[7]','class')

