from page import Page

def test_case_1 (browser):
    page = Page(browser)
    #  Navigate to the URL https://www.sogeti.com/
    page.load()
    #  Hover over Services Link
    page.hover('//*[@id="header"]/div[1]/nav/ul/li[3]/div')

    #  and then Click Automation link.
    page.click('//*[@id="header"]/div[1]/div[5]/ul/li[7]/a')

    #  On Automation Page, scroll down to the Contact us Form.
    page.scroll_into_view('//*[@id="99a12a58-3899-4fe1-a5c7-b9065fe635b0"]')

    #  Fill the First Name with Random Generated Data.
    page.input_to('//*[@id="4ff2ed4d-4861-4914-86eb-87dfa65876d8"]','test')

    #  Fill the Last Name with Random Generated Data
    page.input_to('//*[@id="11ce8b49-5298-491a-aebe-d0900d6f49a7"]','test')

    #  Fill the Email with Random Generated Data
    page.input_to('//*[@id="056d8435-4d06-44f3-896a-d7b0bf4d37b2"]','test@test.test')

    #  Fill the Phone with Random Generated Data
    page.input_to('//*[@id="755aa064-7be2-432b-b8a2-805b5f4f9384"]','test')

    #  Fill the Message with Random Generated Data
    page.input_to('//*[@id="88459d00-b812-459a-99e4-5dc6eff2aa19"]','test')

    #  Check the I agree checkbox.
    page.click('//*[@id="863a18ee-d748-4591-bb64-ef6eae65910e"]/label/input')

    #  Then Click SUBMIT button.
    page.click('//*[@id="06838eea-8980-4305-83d0-42236fb4d528"]')

    #  After clicking SUBMIT button the form is submitted and Thank you message is displayed. Assert the Thank you message
    assert 'Thank you for contacting us.' in page.get_attribute_of_element('//*[@id="99a12a58-3899-4fe1-a5c7-b9065fe635b0"]/div[1]/div/p','textContent')